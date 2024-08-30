import requests
from bs4 import BeautifulSoup

class listConferences():
    def __init__(self, url) -> None:
        """list all talks for the given url

        Parameters
        ----------
        url : str
            Url for the session we want to pull talks from
        """
        self.url = url

    def listAllConferences(self) -> list:
        """list all talk urls for a given session

        Returns
        -------
        list
            returns a list of talk urls for a given session of conference
        """
        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="libraryGridLayout-AAbjO")
        # conference = soup.find("title")
        job_elements = results.find_all('a', href=True)
        conference_urls = []
        for element in job_elements:                
            if "/study/general-conference/" in element['href'] and "lang=eng" in element['href'] and not "speakers" in element['href']:
                if "/04?" in element['href'] or "/10?" in element['href']:
                    conference_urls.append("https://www.churchofjesuschrist.org" + element['href'])
        return conference_urls