import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("stats.csv", nrows=21, delimiter=';')


weeks = df['Week #'].values
x = np.arange(len(weeks))
w = 0.3
plt.bar(x-w, df['Demand'].values, width=w, label='Demand')
plt.bar(x, df['Inv level'].values, width=w, label='Inventory level')
plt.bar(x+w, df['Cost at E.o.W'].values, width=w, label='Total week cost')
plt.xticks(x, weeks)
plt.tight_layout()
plt.xlabel('Number of week')
plt.ylabel('Amount')
plt.legend(['Demand' , ' Inventory level ', ' Weekly Cost']) # demand is blue, inventory orange, cost is green
plt.savefig("CSVBarplots.png", bbox_inches="tight") #saving plot to a png
plt.show()
