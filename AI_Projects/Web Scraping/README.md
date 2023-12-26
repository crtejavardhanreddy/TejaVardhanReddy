
# Web Scraping

The objective of the Web Scraping is to extract the required number of links from the given website link recursively and to scrape all the text content available in each and every website.






## Code overview

>This code consists of two parts.
    Links extraction,
    Text scraping

>Inputs:
    Website URL, 
    Maximum number of URLs to be stored,
    Number of URLs to be extracted from each website

>Output:
    Extracted_links.txt file storing all the available links.
    Content.txt file which is storing all the text data available.


## Link Extraction
It mainly focuses on the extraction of valid and unique URLs from the given website.

- The code begins with extraction of the <Number_of_URLs>(input) from each website
- Then its goes with the above process for the each URL extracted until it reaches <Max_Urls>(input).
 
## Text Scraping

- After the <Max_URLs> got saved in liks_extracted.txt file, the text Scraping starts for each child_URL and saved in Content.txt file.
## Get Started
> To begin with creation of virtual environment
    python -m venv <environment name>
>Secondly install the dependencies
    pip install -r requirements.txt
>Finally execute the main file
    python run main.py

- This displays the gradio interface in which inputs are asked.
- The output fils will be stored in the current working directory.
## Dependencies
- [Gradio](https://www.gradio.app/)
- [langchain document_loaders](https://python.langchain.com/docs/integrations/document_loaders/recursive_url)
- [langchain document_transformers](https://python.langchain.com/docs/integrations/document_transformers/beautiful_soup)
- [beautiful soup 4](https://pypi.org/project/beautifulsoup4/) 
- [requests](https://pypi.org/project/requests/)
- [re (regular expressions)](https://docs.python.org/3/library/re.html)

> **Note:** The usage of anti-webscraping tools of the input website does not scrap the links and text.
