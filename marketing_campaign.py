from unittest.mock import inplace

import pandas as pd
from datetime import datetime

df = pd.read_excel("c:/Users/Lenovo/OneDrive/Desktop/marketing_campaign.xlsx")
print(df.head())

#checking for null values
null = df.isnull().sum()
print(null)

#dropping null values
df.dropna(subset = ['Income'], inplace=True)
print(df['Income'].isnull().sum())

#checking for duplicate values
duplicate_value = df.duplicated().sum()
print(duplicate_value) # no duplicate values

# converting to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format = '%d-%m-%y')
print(df['Dt_Customer'].dtype)

#creating new column for customer tenure
df['customer_tenure'] = datetime.now().year - df['Dt_Customer'].dt.year
print(df.head())

#standardizing text columns
df["Education"] = df["Education"].str.strip().str.replace(' ','_', regex = False)

df['Marital_Status'] = df['Marital_Status'].str.strip().str.replace(' ','_',regex=False)
df['Marital_Status'] = df['Marital_Status'].str.replace('Alone','Single')

#converting all columns in lowercase
df.columns = df.columns.str.lower()
print(df.head())

#checking for datatypes of each columns
print(df.info())

#exporting dataframe to excel
df.to_excel('cleaned_marketing_campaign.xlsx', index=False)
