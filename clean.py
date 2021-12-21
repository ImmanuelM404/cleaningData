import pandas as pd 


#Clean Data 

#Step 1: Understanding Your Data 
data = pd.read_csv('artwork_sample.csv')
print(data.head())

print(data.dtypes)