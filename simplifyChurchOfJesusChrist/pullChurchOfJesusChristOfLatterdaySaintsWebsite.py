import requests
import os, re
from bs4 import BeautifulSoup

class simplerTalks():
    def __init__(self, urlExtension: str, folderPath: str) -> None:
        """pull each talks plain text then save to a text file

        Parameters
        ----------
        urlExtension : str
            the url extension for the session containing 
            the talks you want to copy
        folderPath : str
            the file path where you want the plain text files saved
        """
        self.urlExtension = urlExtension
        self.folderPath = folderPath

    def writeSpecificTalk(self) -> None:
        """pull text for each talk in the given session,
           and save it as a plain text file in the user
           specified location.
        """
        URL = "https://www.churchofjesuschrist.org" + self.urlExtension
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="body")
        talk_name = soup.find("title")
        clean_talk_Name = re.sub('\W+', ' ', talk_name.text.strip())
        job_elements = results.find_all("p")

        if os.path.isfile(self.folderPath + '/' + clean_talk_Name + '.txt'):
            print("The file" , clean_talk_Name.strip() + '.txt', "already exists")
        else:
            with open(self.folderPath + '\\' + clean_talk_Name.strip() + '.txt', 'w', encoding='utf-8') as f:
                f.write(clean_talk_Name + '\n')
                for element in job_elements:
                    f.write(element.text.strip() + '\n')