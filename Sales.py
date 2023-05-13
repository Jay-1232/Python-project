import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv("Advertising.csv")
# Shows of represents the Csv file in a Tabular Form 
sales.head
# Gives the information of the columns of the table
sales.info()
# Calculates and Describes the count, mean , std , min, 25%, 50%, 75%, max 
sales.describe()
#  Show the size or dimension of table
sales.shape
