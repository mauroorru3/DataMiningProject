import math
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys

# Option to show all columns (without these options pycharm show me few columns):
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

from collections import defaultdict
from scipy.stats.stats import pearsonr



# Loading the data set

print("Opening the file")

df = pd.read_csv('customer_supermarket.csv', sep='\t', index_col=0)

print("File opened")

print(df.head())
print()
print(df.tail())

#Types of Attributes and basic checks


print()
print("Features types")
print(df.dtypes)
print()
print("Features info")
print(df.info())

# Check the values of the first element

print()
print("First elements values:")
print(df.iloc[0])


# Basic Statistics
print()
print("Statistics:")
print(df.describe())

"""
Per sostituire dei valori:
df["total_bill"].replace({"aaaaa": 0}, inplace=True)
"""


# Different values per feature

print("Distinct Values in BasketID: \t", df.BasketID.unique())
print("Distinct Values in BasketDate:\t", df.BasketDate.unique())
print("Distinct Values in Sale: \t", df.Sale.unique())
print("Distinct Values in CustomerID: \t", df.CustomerID.unique())
print("Distinct Values in CustomerCountry: \t", df.CustomerCountry.unique())
print("Distinct Values in ProdID:\t", df.ProdID.unique())
print("Distinct Values in ProdDescr: \t", df.ProdDescr.unique())
print("Distinct Values in Qta: \t", df.Qta.unique())

print("Number of distinct Values in BasketID: ", len(df.BasketID.unique()))
print("Number of distinct Values in BasketDate: ", len(df.BasketDate.unique()))
print("Number of distinct Values in Sale: ", len(df.Sale.unique()))
print("Number of distinct Values in CustomerID: ", len(df.CustomerID.unique()))
print("Number of distinct Values in CustomerCountry: ", len(df.CustomerCountry.unique()))
print("Number of distinct Values in ProdID:", len(df.ProdID.unique()))
print("Number of Distinct Values in ProdDescr: ", len(df.ProdDescr.unique()))
print("Number of Distinct Values in Qta: ", len(df.Qta.unique()))


# Missing Values Detection

print()
print(df.isnull().any())


# Correlation

print()

# Scatter Plot & Scatter Matrix

print()


# Distributions


print()

# Replace Missing Values

print()
print("Missing values for CustomerID")
print(df[df['CustomerID'].isnull()])
print("Number of missing values for CustomerID: ", df['CustomerID'].isnull().sum())
print()
print("Missing values for ProdDescr")
print(df[df['ProdDescr'].isnull()])
print("Number of missing values for ProdDescr: ", df['ProdDescr'].isnull().sum())

# Box plots


print()


sys.exit(0)

