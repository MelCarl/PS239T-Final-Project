
# coding: utf-8

# In[ ]:

#In this document, I use Python to code a webscraper 
#that takes data from Wikipedia's List of Sieges and
#produces a csv file that has the siege name, war 
#during which it occcured, the date of the seige,
#and extra detail about who initiated the siege.


# In[2]:

#Import required modules
import requests
from bs4 import BeautifulSoup
import os
import re
import csv
from operator import itemgetter
from itertools import groupby


# In[3]:

#Make a GET request
req = requests.get('https://en.wikipedia.org/wiki/List_of_sieges')

#Read the content of the server’s response
src = req.text

#Soup it
soup = BeautifulSoup(src, "lxml")
#print(soup.prettify())


# In[5]:

#Get all ul elements
rows = soup.find_all("ul")
print(rows)


# In[6]:

#Subset the above rows to get only the modern sieges (from 1800s to the present)
modernsieges = rows[26:28]

#print(modernsieges)
#type(modernsieges)


# In[7]:

#Keep only the text in each of those cells
rowData = [cell.text for cell in modernsieges]
#print(rowData)
#type(rowData)


#Split at each \n to return a list of lines
for line in rowData:
        modSiege = line.split("\n")
        #print(Siege)

#Get the number of elements in the list
len(modSiege)

#Get rid of first and last elements, which are blank
FinalListofSieges = modSiege[1:77]  
#Print(FinalListofSieges)

#Export as csv
import pandas as pd
my_df = pd.DataFrame(FinalListofSieges)
my_df.to_csv('1-ListofSiegesScrapedfromWikipedia.csv', index=False, header=False)


