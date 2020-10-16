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



sys.exit(0)