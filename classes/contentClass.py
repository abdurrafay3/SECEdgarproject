from typing import Optional,  List
from bs4 import BeautifulSoup
import requests


class Content:
    """This is the class for each datapoint. It contains the content of a pdf which it gets by calling multiple helper functions"""

    texts_list: List[str] 
    accession_with_dashes: str
    accession_without_dashes: str
    base_url: str
    json_url: str

    def __init__(self, datapoint: dict):
        """
        This function initializes the object
        """
        self.headers = {"User-Agent": "abdurrafay102003@gmail.com"}
        self.cik = datapoint["cik"]
        self.accession_with_dashes = datapoint.get("accessionNumber")
        self.accession_without_dashes = self.accession_with_dashes.replace("-", "")
        self.json_url = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{self.accession_without_dashes}/index.json"
        self.text_list = self.get_text()

    def get_text(self) -> List[str]:
        """
        This function gets the content from the website using regex and other methods
        """
        txt_list = []
        json_object = self.get_json_object()
        for item in json_object['directory']['item']:
            if item['name'].endswith(".txt"):
                text_file_url = self.get_url_to_text(item['name'])
            else:
                text_file_url = None
        #text_file_url = self.get_url_to_text()
        if text_file_url is not None:
            content_website = requests.get(text_file_url, headers=self.headers)
            txt_list.append(content_website.text)
        else:
            content_website = None
        return txt_list
        # ? we have obtained the content and now we can extract the content

    def get_json_object(self):
        json_object = requests.get(self.json_url, headers=self.headers).json()
        return json_object

    def get_url_to_text(self, name_file : str):
        url_to_text = self.json_url.rsplit("/", 1)[0] + "/" + name_file
        return url_to_text
