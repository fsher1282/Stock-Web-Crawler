import requests
from bs4 import BeautifulSoup

class AbstractScrapper(object):
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")