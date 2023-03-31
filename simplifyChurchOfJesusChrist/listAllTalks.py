import requests
from bs4 import BeautifulSoup

URL = "https://www.churchofjesuschrist.org/study/general-conference/2022/10?lang=eng"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="body")
job_elements = results.find_all('a', href=True)
for element in job_elements:
    print(element['href'])