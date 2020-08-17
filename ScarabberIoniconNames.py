# Get the names of All Ionicons Version 4 & Write them to a text file 
from bs4 import BeautifulSoup
import requests
import pathlib
import os

# declare an empty array
iconsArray = []
URL = 'https://ionicons.com/v4/cheatsheet.html'

# fetching the whole html page
thePage = requests.get(URL)

# the content we need
pageContent = BeautifulSoup(thePage.content, 'html.parser')

# from content findAll nodes that match this
filterdResults = pageContent.findAll('tr',{'class':"mode-row"})

# get current file path 
textFilePath = pathlib.Path(__file__).parent.absolute()

# join path to get full text file path 
fullTextFilePath = os.path.join(textFilePath ,"ScarabberIoniconNames.txt")

# join path and Open text file we Writing to
textFile = open(fullTextFilePath, "w")

#loop throught the filterdResults
for x in filterdResults:

    #  get the specific icon name from the node using attrs
    iconName = x.find('ion-icon').attrs['name']
    
        # below line returna an array of the icons
        # iconsArray.append(iconName)
    # write it to the file
    textFile.write(iconName)
    # append a newline
    textFile.write("\n")
    # print(iconName)

# close the file handle 
textFile.close()

