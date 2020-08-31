import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn


# load data
oecd_bli = pd.read_csv('./datasets/lifesat/oecd_bli_2015.csv', thousands=',')
gdp_per_capita = pd.read_csv('./datasets/lifesat/gdp_per_capita.csv', thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')

# Prepare the data
country_stats = prepare