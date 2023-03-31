import requests
from bs4 import BeautifulSoup

class listTalks():
    def __init__(self, url) -> None:
        self.url = url
        # URL = "https://www.churchofjesuschrist.org/study/general-conference/2022/10?lang=eng"

    def listAllTalks(self) -> list:

        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="body")
        talk_class = soup.find("title")
        job_elements = results.find_all('a', href=True)
        talk_urls = []
        for element in job_elements:
            talk_urls.append(element['href'])
        
        return talk_class.text.strip(), talk_urls