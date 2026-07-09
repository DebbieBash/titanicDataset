import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#Getting to know the data
df = pd.read_csv("titanic/train.csv")
print(df.head)


# Display all column names
#print(df.columns)
#print(df.info())
#print(df.describe(include="all"))
#print(df.isnull().sum())

#see duplicate data
#print(df.duplicated().sum())

#


#_______________________________________________________________________________________
##Data Cleaning

#Convert names to lower case
df["Name"] = df["Name"].str.lower()


#Fill missing age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())


#Remove rows with missing values
df = df.dropna()
print(df.isnull().sum())


# Count duplicate rows
df.duplicated().sum()



#Drop unnecessary data
df = df.dropna(subset = ["Cabin"])


df.nunique()
print(df.head())


#_______________________________________________________________________________________
##Data Transformation

#Create copy of data for transformation
df_copy = df.copy()
print(df.head())

# Select specific columns
#df = df[["Survived", "Pclass", "Sex", "Age", "Fare"]]
print(df.head())

#df.rename(columns = {"Pclass": "Passenger_class"}, inplace = True)
#print(df.head)

#sort values
#df = df.sort_values(by="Age", ascending=False)
print(df.tail)


df["Sex"].value_counts()
print(df.head)