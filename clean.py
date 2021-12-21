import pandas as pd 
import re

from pandas.core import indexing


#Clean Data 

#Step 1: Understanding Your Data 
data = pd.read_csv('artwork_sample.csv')
print(data.head())

print(data['title']) #prints the title column 

#Step 2: Remove and Fix Columns 
data.columns = (re.sub(r'([A-Z])', r'_\1', x).upper() for x in data.columns) #watch video about the function re.sub and and import re 
print(data.columns)

print(data.rename(columns={'ARTIST_ROLE':'ROLE'})) #rename column 
    #or could use lameda 
# print(data.rename(columns=lambda x: x.upper()))

#Drop Row 
print(data.drop(columns=['THUMBNAIL_URL', 'URL']))

#Step 3: Idex and Filter 

print(data['TITLE'][0])
year = data[data.ACQUISITION_YEAR > 1800]['ACQUISITION_YEAR']

#indexing with iloc 
artist = (data.loc[:, 'ARTIST'])

artistYear = data.loc[:, ['ARTIST', 'TITLE', 'ACQUISITION_YEAR']]
print(artistYear)


#Handling Bad, Missing Duplicate
