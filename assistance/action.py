from assistance.ioinput import ioinput
import os
import re
import webbrowser
from youtube_search import YoutubeSearch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class action(ioinput):
    chromepath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    wordpath = r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
    excelpath = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
    powerpntpath = r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
    def open(self, inputText):
        """
        This function will open the application requested by the user
        """
        if "chrome" in inputText:
            super().speaker("Opening Chrome")
            os.startfile(self.chromepath)
        elif "word" in inputText:
            super().speaker("Opening Word")
            os.startfile(self.wordpath)
        elif "excel" in inputText:
            super().speaker("Opening Excel")
            os.startfile(self.excelpath)
        elif "powerpoint" in inputText:
            super().speaker("Opening Powerpoint")
            os.startfile(self.powerpntpath)
        elif "youtube" in inputText:
            self.playYoutube(inputText)
        elif "." in inputText:
            self.openwebsite(inputText)
        else:
            super().speaker("This application is not supported")
    def close(self, inputText):
        """
        This function will close the application requested by the user
        """
        if "chrome" in inputText:
            super().speaker("Closing Chrome")
            os.system("taskkill /im chrome.exe /f")
        elif "ie" in inputText:
            super().speaker("Closing IE")
            os.system("taskkill /im iexplore.exe /f")
        elif "word" in inputText:
            super().speaker("Closing Word")
            os.system("taskkill /im WINWORD.EXE /f")
        elif "excel" in inputText:
            super().speaker("Closing Excel")
            os.system("taskkill /im EXCEL.EXE /f")
        elif "powerpoint" in inputText:
            super().speaker("Closing Powerpoint")
            os.system("taskkill /im POWERPNT.EXE /f")
        else:
            super().speaker("This application is not supported")

    def playYoutube(self, inputText):
        """
        Search and open the fisrt video found from Youtube
        """
        pattern = "open (youtube.com)*(youtube)*(.+)*"
        videoname = re.search(pattern, inputText)
        # If no command about the video after youtube then only open youtube.com 
        if videoname.group(3) != None:
            path = YoutubeSearch(videoname.group(3).strip(), max_results=1).to_dict()
            # Get the link of the first result
            self.openwebsite("open youtube.com" + path[0]["url_suffix"])
        else:
            self.openwebsite("open youtube.com")

    def openwebsite(self,inputText):
        """
        This function will open the requested website
        """
        pattern = "open (.+com)(.+)*"
        domain = re.search(pattern,inputText)
        url = "https://www." + domain.group(1)
        if domain.group(2) != None:
            url += domain.group(2)
        # Only output the name of the website
        super().speaker("Opening " + domain.group(1))
        webbrowser.open(url)
    
    def simplecommunication(self, inputText):
        """
        Create a simple communication between the bot and the user
        """
        if "how are you" in inputText:
            super().speaker("I'm doing great. How are you?")
        elif "your name" in inputText:
            super().speaker("My name is Daniel")
        else:
            return False
        return True
