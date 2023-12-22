import gradio as gr
from WebScraping.Link_scraper import LinkScraper
from WebScraping.Text_extractor import TextExtractor

def main(head_url,max_length,num_of_urls):
    try:
        # Web scraping
        web_scraper = LinkScraper(head_url, max_length, num_of_urls)
        web_scraper.Links_Extractor()
        print("All the available links are saved...")

        # Text extraction
        TextExtractor().Extract_text()
        
        print("All the text got scraped")
        acknowledgment = "Web Scraping done..."
        return acknowledgment
    except Exception as e:
        print(f"Error occurres in the main function: {e}")
        return None

if __name__ == "__main__":
#     # Create Gradio interface
    try:
        interface = gr.Interface(
        fn = main,
        inputs = [
            gr.Textbox(label = "URL to Scrape"),
            gr.Slider(label = "Max URLs to scrape", minimum =1, maximum = 10000),
            gr.Slider(label = "Max URLs to scrape from the Website", minimum = 1, maximum = 1000),
        ],
        outputs = [gr.Textbox(label = "Acknowledgment")]
        )

        # Launch Gradio interface

        interface.launch(share = True)
        
    except Exception as e:
        print(f"Error in Gradio: {e}")

"""For more information refer to following document
https://onedrive.live.com/redir?resid=3C855A46E58E3841%21110&authkey=%21ALryIkCEAJjAwLY&page=Edit&wd=target%28Quick%20Notes.one%7Ca272f621-c9fc-4c0c-a387-9d2b24b068ef%2FLinks%20Extraction%7Cf74d4a82-8868-4ebd-9526-23595ac8c37b%2F%29&wdorigin=NavigationUrl
"""