import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fh = open('dane_lista1.txt', 'r')
data1 = fh.readlines()
#plt.hist(data1, bins=20)
#plt.show() 
fh.close()



###pandas
with open('dane_lista1.txt', 'r') as fh:
    data2 = fh.readlines()

df = pd.read_csv('dane_lista1.txt', header=None, names=['value'])
data2 = df['value'].values
plt.hist(data2, bins=20)
plt.show()