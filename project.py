import math
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys

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


sys.exit(0)