import gradio as gr
from Link_scrapper import LinkScrapper
from Text_extractor import TextExtractor

def main(head_url,max_length,num_of_urls):

    # Web scraping
    web_scraper = LinkScrapper(head_url, max_length, num_of_urls)
    web_scraper.Links_Extractor()
    print("All the available links are saved...")

    # Text extraction
    TextExtractor().Extract_text()
    
    print("All the text got scrapped")
    acknowledgment = "Web Scrapping done..."
    return acknowledgment

if __name__ == "__main__":
#     # Create Gradio interface
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

"""For more information refer to following document
https://onedrive.live.com/redir?resid=3C855A46E58E3841%21110&authkey=%21ALryIkCEAJjAwLY&page=Edit&wd=target%28Quick%20Notes.one%7Ca272f621-c9fc-4c0c-a387-9d2b24b068ef%2FLinks%20Extraction%7Cf74d4a82-8868-4ebd-9526-23595ac8c37b%2F%29&wdorigin=NavigationUrl
"""