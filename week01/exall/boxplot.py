import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

s = pd.read_csv("bla.csv")
s = s.replace('_',np.nan).dropna()

fig, axes = plt.subplots(2, 3, figsize=(14, 10))

sns.boxplot(data=s, x="price", ax=axes[0][0])
sns.boxplot(data=s, x="area", ax=axes[0][1])
sns.boxplot(data=s, x="bedrooms", ax=axes[0][2])
sns.boxplot(data=s, x="bathrooms", ax=axes[1][0])
sns.boxplot(data=s, x="stories", ax=axes[1][1])
sns.boxplot(data=s, x="parking", ax=axes[1][2])





plt.xlabel('Values')
plt.ylabel('Frequency')
for i in range(2):
    for j in range(3):
        axes[i][j].xaxis.set_major_formatter(ticker.EngFormatter(unit=''))
plt.show()







