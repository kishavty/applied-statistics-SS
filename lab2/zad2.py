import random
import matplotlib.pyplot as plt
import numpy as np


alpha = 5
lmbda = 2
amount=1000
lista=np.zeros(amount)

#np.random.uniform(size=1000)
for i in range(amount-1):
    lista[i]=(lmbda/(1-random.random())**(1/alpha)-lmbda)

plt.hist(lista)
plt.show()



