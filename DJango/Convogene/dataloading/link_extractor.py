import warnings
import re 
import logging
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup 
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning

# Suppress the warning
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class UrlCollector:

    def __init__(self, head_url: str, max_depth: int, output_file: str):
        self.head_url = head_url
        self.max_depth = max_depth  
        self.output_file = 'Extracted_links.csv'
        self.extracted_urls = set()
        self.visited_urls = set()

    def extract_main_domain(self):
        url = self.head_url
        parsed_url = urlparse(url)
        domain_parts = parsed_url.netloc.split('.')
        if len(domain_parts) > 1:
            main_domain = domain_parts[-2] + '.' + domain_parts[-1]
        else:
            main_domain = domain_parts[0]
        return main_domain

    def is_valid_link(self, url: str, domain_name: str) -> bool:
        image_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg']
        ppt_formats = ['.ppt', '.odp', '.key']
        video_formats = ['.mp4', '.webm', '.ogg', '.avi', '.flv', '.wmv', '.mov']
        other_formats = ['.zip', '.css', '.js', '.csv', '.ico', '.bz2', '.epub', '.woff2']

        if domain_name in url and \
        not any(keyword in url for keyword in image_formats + video_formats + ppt_formats + other_formats) and \
        not any(substring in url.lower() for substring in ["signin", "signup", "login", "search"]):
            return True
        return False    

    def extract_sub_links(self, url, domain_name):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            
            # Ensure the response is HTML
            if 'text/html' not in response.headers.get('Content-Type', ''):
                logger.warning(f"Non-HTML content at URL {url}")
                return
            
            html_document = response.text
            soup = BeautifulSoup(html_document, 'html.parser')  # Try with the default parser first
            
            for link in soup.find_all('a', attrs={'href': re.compile("^https://")}): 
                if self.is_valid_link(link.get('href'), domain_name): 
                    self.extracted_urls.add(link.get('href'))
                    
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
            logger.debug(f"Error occurred while fetching URL {url}: {e}")
        except Exception as e:
            logger.debug(f"Error occurred while parsing URL {url}: {e}")

    def save_extracted_links(self, depth):
        self.extracted_urls.add(self.head_url)
        data = {"doc_urls": list(self.extracted_urls)}
        df = pd.DataFrame(data)
        output_file_with_depth = f"{self.output_file.rsplit('.', 1)[0]}_depth_{depth}.csv"
        df.to_csv(output_file_with_depth, index=False)
        logger.info(f"Extracted links saved to {output_file_with_depth}")

    def links_extractor(self):
        domain_name = self.extract_main_domain()
        urls_to_collect = set([self.head_url])
        
        for depth in range(self.max_depth):
            logger.info(f"Depth {depth + 1}/{self.max_depth}: Processing {len(urls_to_collect)} URLs")
            current_batch = urls_to_collect.copy()
            urls_to_collect.clear()

            with tqdm(total=len(current_batch), desc=f"Depth {depth + 1}", unit="URL") as pbar:
                for url in current_batch:
                    if url not in self.visited_urls:
                        self.visited_urls.add(url)
                        self.extract_sub_links(url, domain_name)
                        pbar.update(1)
                
                urls_to_collect.update(self.extracted_urls - self.visited_urls)
                self.save_extracted_links(depth + 1)

        logger.info(f"Total links collected: {len(self.extracted_urls)}")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="URL Collector")
#     parser.add_argument("--head_url", type=str, help="Provide a Head URL")
#     parser.add_argument("--max_depth", type=int, default=1, help="Maximum number of depth")
#     parser.add_argument("--output_file", type=str, default="Extracted_links.csv", help="Path to save the extracted links")
#     args = parser.parse_args()
# collector = UrlCollector(head_url, max_depth)
#     collector.links_extractor()
