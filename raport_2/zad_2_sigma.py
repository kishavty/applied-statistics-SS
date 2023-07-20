import numpy as np
import pandas as pd
from scipy.stats import chi2
import matplotlib.pyplot as plt
from scipy.special import gammainc


df = pd.read_csv('lista8_zad2.csv',header=None)

ALPHA = 0.05
HYPOTHESIS = 1.5
MEAN = df.mean(0)[0]
VAR = df.var(0)[0]
TEST_CHI2 = ((df.size - 1) * VAR) / HYPOTHESIS

### do wykresu
t = np.linspace(800, 1200, 10**4)
pdf = chi2.pdf(t, df.size - 1)

### a) sigm^2 != 1.5

lower_critical = chi2.ppf(ALPHA/2, df.size - 1)
upper_critical = chi2.ppf(1 - ALPHA/2, df.size - 1)
p_value_a = 2 - chi2.cdf(TEST_CHI2, df.size - 1) * 2

print(f'[{lower_critical}; {upper_critical}]')  #przedział akceptacji
print(f'p_a = {p_value_a}')  #p-wartość

plt.plot(t, pdf, label='Gęstość rozkładu $\chi^2_{999}$')
plt.fill_between(t, 0, pdf, where=(t < lower_critical) | (t > upper_critical), label='Obszar krytyczny')
plt.axvline(x=TEST_CHI2, color='black', linestyle="dashed", alpha=0.7, label="Statystyka testowa $\chi^2$")
plt.xlabel('x')
plt.ylabel('Gęstość rozkładu')
plt.legend()
plt.show()


### b) sigm^2 > 1.5

upper_critical_b = chi2.ppf(1 - ALPHA, df.size - 1)
p_value_b = 1 - chi2.cdf(TEST_CHI2, df.size - 1)

print(f'[-inf; {upper_critical_b}]')  #przedział akceptacji
print(f'p_b = {p_value_b}')  #p-wartość

plt.plot(t, pdf, label='Gęstość rozkładu $\chi^2_{999}$')
plt.fill_between(t, 0, pdf, where=(t > upper_critical_b), label='Obszar krytyczny')
plt.axvline(x=TEST_CHI2, color='black', linestyle="dashed", alpha=0.7, label="Statystyka testowa $\chi^2$")
plt.xlabel('x')
plt.ylabel('Gęstość rozkładu')
plt.legend()
plt.show()


### c) sigm^2 < 1.5

lower_critical_c = chi2.ppf(ALPHA, df.size - 1)
p_value_c = gammainc((df.size - 1) / 2, TEST_CHI2 / 2)

print(f'[{lower_critical_c}; inf]')  #przedział akceptacji
print(f'p_c = {p_value_c}')  #p-wartość

plt.plot(t, pdf, label='Gęstość rozkładu $\chi^2_{999}$')
plt.fill_between(t, 0, pdf, where=(t < lower_critical_c), label='Obszar krytyczny')
plt.axvline(x=TEST_CHI2, color='black', linestyle="dashed", alpha=0.7, label="Statystyka testowa $\chi^2$")
plt.xlabel('x')
plt.ylabel('Gęstość rozkładu')
plt.legend()
plt.show()