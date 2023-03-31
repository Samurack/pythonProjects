import requests
import os, re
from bs4 import BeautifulSoup
################################below we need to have the URL be https://www.churchofjesuschrist.org/
################################we then need to append the talk from listAllTalks.py
################################lastly we need to save each pull into its own text file.
class simplerTalks():
    def __init__(self, urlExtension: str, folderPath: str) -> None:
        self.urlExtension = urlExtension
        self.folderPath = folderPath

    def writeSpecificTalk(self) -> None:

        URL = "https://www.churchofjesuschrist.org" + self.urlExtension
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="body")
        talk_class = soup.find("title")
        cleanName = re.sub('\W+', '', talk_class.text)
        job_elements = results.find_all("p")

        if os.path.isfile(self.folderPath + '/' + cleanName + '.txt'):
            print("The file" , cleanName + '.txt', "already exists")
        else:
            print("Adding talk", cleanName)
            with open(self.folderPath + '/' + cleanName + '.txt', 'w', encoding='utf-8') as f:
                f.write(cleanName + '\n')
                for element in job_elements:
                    f.write(element.text.strip() + '\n')
