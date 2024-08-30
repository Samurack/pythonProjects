import requests
from bs4 import BeautifulSoup

class listTalks():
    def __init__(self, url) -> None:
        """list all talks for the given url

        Parameters
        ----------
        url : str
            Url for the session we want to pull talks from
        """
        self.url = url

    def listAllTalks(self) -> list:
        """list all talk urls for a given session

        Returns
        -------
        list
            returns a list of talk urls for a given session of conference
        """
        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="body")
        talk_name = soup.find("title")
        job_elements = results.find_all('a', href=True)
        talk_urls = []
        for element in job_elements:
            talk_urls.append(element['href'])
        return talk_name.text.strip(), talk_urls