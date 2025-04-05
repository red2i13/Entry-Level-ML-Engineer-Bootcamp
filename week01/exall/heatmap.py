import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan).dropna()

sns.set_style('darkgrid')
g = sns.heatmap(s[['price', 'area', 'bathrooms', 'bedrooms', 'parking', 'stories']].corr())


plt.show()



