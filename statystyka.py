import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
 
data = np.random.normal(10, 3, 10000) #Generating data randomly from a normal distribution.
 
sb.set_style("whitegrid")  # Setting style(Optional)
plt.figure(figsize = (10,5)) #Specify the size of figure we want(Optional)
sb.distplot(x = data  ,  bins = 10 , kde = True , color = 'teal'\
             , kde_kws=dict(linewidth = 4 , color = 'black'))
plt.show()