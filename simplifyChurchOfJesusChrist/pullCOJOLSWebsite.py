import requests
from bs4 import BeautifulSoup
################################below we need to have the URL be https://www.churchofjesuschrist.org/
################################we then need to append the talk from listAllTalks.py
################################lastly we need to save each pull into its own text file.
URL = "https://www.churchofjesuschrist.org/study/general-conference/2022/10/18oaks?lang=eng"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="body")
job_elements = results.find_all("p")
for element in job_elements:
    print(element.text.strip())