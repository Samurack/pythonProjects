from listAllTalks import listTalks
from pullCOJOLSWebsite import simplerTalks
import os

talksUrl = input("What's the url for the list of talks we are pulling? ")
# talksUrl = "https://www.churchofjesuschrist.org/study/general-conference/2022/10?lang=eng"

folderName, allTalks = listTalks(talksUrl).listAllTalks()
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, folderName)
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

for talk in allTalks:
    simplerTalks(talk, final_directory).writeSpecificTalk()