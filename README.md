#PS239T-Final-Project
Melissa Carlson
December 11, 2016
 
Short Description

My PS239T final project focused on collecting descriptive data and producing visualizations of governments' and rebel groups' use of siege tactics against civilian and military targets in modern wars. To collect this data, I used Python to write a webscraper that pulls data on use of sieges in modern wars from Wikipedia's 'List of Sieges.' I then use R to clean this data, which produced several data sets (see below for further descriptions). Lastly, I used R to visualize this descriptive data in four graphs, including two scatter plots that show use of sieges over time in modern wars and specifically in Syria, one line graph that shows the relationship (or lack thereof) between war duration and use of siege tactics, and one map, which has geographic locations of the sieges in Syria. 

Dependencies

My code depends on the following software:
R, version 3.1
Python version 3.5.2, Anaconda 4.1.1

My code also depends on installing the following packages in Python:
requests
BeautifulSoup
os
re
csv
itemgetter
groupby

My code also depends on installing the following packages in R:
foreign
dplyr
tidyr
maps      
mapdata 
rgdal
rgeos
maptools
tmap
ggplot2

Files

Below I list all of the files contained in this repository with brief descriptions, categorized by Data, Code, and Results:

Data

1-ListofSiegesScrapedfromWikipedia.csv: Contains the data, specifically list of sieges and relevant descriptive information about each siege, that I scraped from Wikipedia's 'List of Sieges,' which can be found at https://en.wikipedia.org/wiki/List_of_sieges

2-SiegeList-Cleaned.csv: Contains the first cut at the cleaned data from Wikipedia, with three variable columns (SiegeName, Year, and WarName). Because this has several errors that I need to manually correct, and I have extra data columns that I want to add, I export this data frame on line 45 of 02_DataCleaning.R.Rmd.

3-SiegeList-Cleaned-additions.csv: Contains the data from 2-SiegeList-Cleaned.csv, except I have manually corrected several errors I could not correct using R, and have added a data column coding whether the war was an Interstate or Civil war. I reload this data back into 02_DataCleaning.R.Rmd on line 48. 

4-SiegeperWar.csv: Contains the data frame, with each modern war as the observations, and the columns as the number of sieges that have occurred in each war. I export this data frame on line 57 of 02_DataCleaning.R.Rmd in order to add an additional data column of whether the war was Interstate or Civil. 

5-SiegeperWar-additions.csv: I import the data from 4-SiegeperWar.csv, with the additional data column of Interstate_orCivil on line 58 of 02_DataCleaning.R.Rmd. 

6-SyrianCivilWarSiegeList.csv: Filtering the data from 3-SiegeList-Cleaned-additions.csv, this data set contains only sieges that occurred during the Syrian civil war. I export this data set on line 103 of 03_DataVisualization_R.Rmd to add two additional data columns on whether the sieges were initiated by the government or rebels, and whether they targeted civilians or military personnel.

7-SyrianCivilWarSiegeList-additions.csv: This contains the data from 6-SyrianCivilWarSiegeList.csv with the two additional data columns on whether the sieges were initiated by the government or rebels, and whether they targeted civilians or military personnel. This is loaded into 03_DataVisualization_R.Rmd on line 104.

8-SyrianCivilWarSiegeList-mapdata.csv: This contains the data from 7-SyrianCivilWarSiegeList-additions.csv, with two added columns of the longitude and latitude of the towns and military bases where the sieges occurred in Syria. This data set is loaded in on line 138 of 03_DataVisualization_R.Rmd. 

Code

01_Webscraping_Python.py: Collects data from the Wikipedia page 'List of Sieges' and exports the data to the file 1-ListofSiegesScrapedfromWikipedia.csv

02_DataCleaning_R.Rmd: Loads and cleans the data from 1-ListofSiegesScrapedfromWikipedia.csv. This script produces the data sets found above. Throughout the course of cleaning the data, I needed to fix errors manually, or add additional data, which necessitated that I exported and re-imported the data. I included all data sets, both the ones I exported and re-imported. There are four final data sets which I use for visualization: 3-SiegeList-Cleaned-additions.csv, 5-SiegeperWar-additions.csv, 7-SyrianCivilWarSiegeList-additions.csv, and 8-SyrianCivilWarSiegeList-mapdata.csv. I included the other data sets to demonstrate the process of cleaning the data and adding additional relevant information.

03_DataVisualization_R.Rmd: Conducts descriptive analysis of the data, producing the visualizations (graphs and maps) found in the Results directory.

Results

Graph1_UseofSiegesinModernWarfare.jpg: Graphs the number of sieges used in modern wars over time. The x-axis is the start date of the war, and the y-axis is the number of sieges used per war. The points vary in size depending on the number of sieges used in a given war, and in color depending on war type (civil war or interstate war).

Graph2_WarDurationandNumberofSieges.jpg: Graphs the correlation between the duration of a war and the number of sieges used in that war, including a bivariate regression line and points for each war, colored depending on war type (civil war or interstate war).

Graph3_SiegesinSyrianCivilWar.jpg: Graphs the sieges that have occurred in the Syrian civil war, with the start date of the siege on the x axis and the end date on the y-axis, showing which sieges lasted the longest. The points for each siege vary in shape (triangle for government initiated, circle for rebel initiated) and color (red for civilian target, black for military target).

Graph4_SyriaSiegesMap.jpg: Maps the location of sieges in Syria, with each point varying in color (red/pink for civilian target, blue for military target) and shape (triangle for government initiated, circle for rebel initiated).

More Information

If you have any questions or comments about reproducing the results outlined above, please contact Melissa Carlson at m.a.carlson@berkeley.edu. 