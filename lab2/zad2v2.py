import random
import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

alfa = 5
lamba = 2
amount=1000
value=(lamba/(1-np.random.uniform(0, 1, amount))**(1/alfa)-lamba)
plt.hist(value)
plt.show()
