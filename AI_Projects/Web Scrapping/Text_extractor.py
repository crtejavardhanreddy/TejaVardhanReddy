import PyPDF2
import os
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.document_transformers import BeautifulSoupTransformer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from langchain.document_loaders import PyPDFLoader


# It reads all the text available in the website and store in a text file 
class TextExtractor:
    def __init__(self,max_depth = 2, path_to_save_links="./Extracted_links.txt", path_to_save_text="./Content.txt"):
        self.max_depth = max_depth
        self.path_to_save_links = path_to_save_links
        self.path_to_save_text = path_to_save_text 

    # RecursiveUrlLoader is a method to load all URLs under a root directory and is provided by langchain
    # BeautifulSoupTransformer is a method for parsing HTML content
    def Text_Extractor(self, url):
        loader = RecursiveUrlLoader(url=url, max_depth=self.max_depth)
        bs_transformer = BeautifulSoupTransformer()
        docs = bs_transformer.transform_documents(loader.load(), tags_to_extract=["p"])
        return docs

    # The links are loaded from a text file
    def Load_links(self):
        with open(self.path_to_save_links, "r", encoding="utf-8") as file:
            links = [link.strip() for link in file.readlines()]
        return links

    # The text extraction and saved to a specified file
    def Extract_and_save_text(self, links):
        file_path = self.path_to_save_text
        if os.path.exists(file_path):
            os.remove(file_path)

        for link in links:
            docs = self.Text_Extractor(link)
            with open(self.path_to_save_text, "+a", encoding="utf-8") as f:
                for doc in docs:
                    f.write(doc.page_content + "\n")

            return docs
        
    def Save_pdf(self,docs):
        pdf_writer = PyPDF2.PdfWriter()

        for page in docs:
            pdf_writer.add_page(page)

        with open("Content.pdf","wb") as f:
            pdf_writer.write(f)
        
    def Extract_text(self):
        links = self.Load_links()
        docs = self.Extract_and_save_text(links)
        self.Save_pdf(docs)
        return docs
    
    # Extract_text()