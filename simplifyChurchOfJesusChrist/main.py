from listAllTalks import listTalks
from pullChurchOfJesusChristOfLatterdaySaintsWebsite import simplerTalks
from listAllConferences import listConferences
import os
"""This program is mean to pull all talks from one 
   one specific session of conference and convert
   them into text files, saving them to a folder
   named after the session of conference we chose.
"""
# ConferencesUrl = input("What's the url extension for the conference talks? ")
ConferencesUrl = "https://www.churchofjesuschrist.org/study/general-conference?lang=eng"
conferences = listConferences(ConferencesUrl).listAllConferences()

for conference in conferences:
   print("conference", conference)
   folderName, allTalkUrls = listTalks(conference).listAllTalks()

   current_directory = os.getcwd()
   final_directory = os.path.join(current_directory, folderName)
   if not os.path.exists(final_directory):
      os.makedirs(final_directory)

   for talk in allTalkUrls:
      simplerTalks(talk, final_directory).writeSpecificTalk()