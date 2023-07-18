import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

n = 1000

#r. normalny
mu = 0  #średnia
sigma = 1  #odchylenie standardowe

#lognormalny
s = 0.5  
sigma_ln = 0.5  #odchylenie standardowe

#pareto
alpha = 2

#próby
""""sample_normal = np.random.normal(mu, sigma, size=n)
sample_lognormal = np.random.lognormal(mean=mu, sigma=sigma_ln, size=n)
sample_pareto = pareto.rvs(alpha, size=n)

#statystyki U
U_normal = np.max(sample_normal)
U_lognormal = np.max(sample_lognormal)
U_pareto = np.max(sample_pareto)"""


num_trials = 1000 # liczba prób
data_normal = []
data_lognormal = []
data_pareto = []
for i in range(num_trials):
    samples_normal = np.random.normal(mu, sigma, size=n)
    samples_lognormal = np.random.lognormal(mean=mu, sigma=sigma_ln, size=n)
    samples_pareto = pareto.rvs(alpha, size=n)

    U_normal = np.max(samples_normal)
    U_lognormal = np.max(samples_lognormal)
    U_pareto = np.max(samples_pareto)

    data_normal.append(U_normal)
    data_lognormal.append(U_lognormal)
    data_pareto.append(U_pareto)



#dystrybuanta empirycznych
plt.figure(figsize=(10, 6))
plt.hist(data_normal, bins='sqrt', density=True, alpha=0.5, label='Normalny')
plt.legend()
plt.xlabel('Wartość statystyki U')
plt.ylabel('Dystrybuanta empiryczna')
plt.title('Dystrybuanty empiryczne statystyki U dla danych rozkładów')
plt.show()

plt.hist(data_lognormal, bins='sqrt', density=True, alpha=0.5, label='Lognormalny')
plt.legend()
plt.xlabel('Wartość statystyki U')
plt.ylabel('Dystrybuanta empiryczna')
plt.title('Dystrybuanty empiryczne statystyki U dla danych rozkładów')
plt.show()

plt.hist(data_pareto, bins='sqrt', density=True, alpha=0.5, label='Pareto')
plt.legend()
plt.xlabel('Wartość statystyki U')
plt.ylabel('Dystrybuanta empiryczna')
plt.title('Dystrybuanty empiryczne statystyki U dla danych rozkładów')
plt.show()
#plt.axvline(U_normal, color='b', linewidth=2, label=f'U = {U_normal:.2f}')
#plt.axvline(U_lognormal, color='orange', linewidth=2, label=f'U = {U_lognormal:.2f}')
#plt.axvline(U_pareto, color='g', linewidth=2, label=f'U = {U_pareto:.2f}')
