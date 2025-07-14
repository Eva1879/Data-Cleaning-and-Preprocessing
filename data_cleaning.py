# Import pandas library functions for analysis & manipulation, shortnamed as pd
import pandas as pd
import numpy as np

# Load the CSV file 
load = pd.read_csv("research-and-development-survey-2024.csv")

# Show the first few rows
#print(load.head())

# Shows a summary of the dataset
#print(load.info())
#print(load.describe(include='all'))

# Checking and displaying any missing entry: counts the NaN's values for the correspinding column name
print(load.isnull().sum())

#Checks for any imp value in the Status column
print(load['Status'].unique())

#Drop the entire column of 'Status' as most are NaN's and not needed
load=load.drop(columns=["Status"])
#Drop any remaining rows
load=load.dropna()

#Impute with mean, median, mode: of numeric datatype Year; fills the empty rows with the avg of the years, usable data
load['Year']=load['Year'].fillna(load['Year'].mean())

print(load['Year'])
#print(load.dtypes)

# Remove duplicate rows and standardize inconsistent data formats (e.g., date formats, categorical variables).
# Remove duplicate rows
load = load.drop_duplicates()


# Example for standardizing a categorical column like 'Unit' & 'Footnotes'
load['Unit'] = load['Unit'].str.strip().str.title()

print(load['Unit'])

#3 and 12 becomes 3,12; likewise 12 and 3 become 12,3
def standardize_footnotes(val):
    parts = sorted(val.replace(' and ', ',').split(','))
    return ','.join(part.strip() for part in parts)

load['Footnotes'] = load['Footnotes'].apply(standardize_footnotes)

print(load['Footnotes'])

#Standardize 'R' as missing
load['RD_Value'] = load['RD_Value'].replace({'R': np.nan, '...': np.nan})

print(load['RD_Value'])








