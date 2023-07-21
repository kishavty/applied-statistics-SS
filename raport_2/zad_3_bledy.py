import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd


ALPHA = 0.05
MU = 1.5
SIGMA = 0.2

df = pd.read_csv("lista8_zad2.txt", header=None, names=["a"])

Z = (df["a"].mean() - MU) * np.sqrt(len(df)) / SIGMA

def plot(x, y, quantile, Z_value, title):
    plt.plot(x, y, label="Gęstość rozkładu N(0,1)")
    if title == "a) mu != 1.5":    
        plt.fill_between(x, 0, y, where = (x > quantile), color = "r", label="Obszar krytyczny")
        plt.fill_between(x, 0, y, where = (x < -quantile), color = "r")
    if title == "b) mu > 1.5":
        plt.fill_between(x, 0, y, where = (x > quantile2), color = "r", label="Obszar krytyczny")
    if title == "c) mu < 1.5":    
        plt.fill_between(x, 0, y, where = (x < -quantile2), color = "r",label="Obszar krytyczny")
    plt.xlabel("x")
    plt.ylabel("Gęstość rozkładu N(0,1)")
    plt.legend()
    plt.title(title)
    plt.show()


### a) mu != 1.5
row = 1 - ALPHA / 2
quantile = st.norm.ppf(row, 0, 1)
p_value1 = 2 - 2 * st.norm.cdf(abs(Z))


x = np.arange(-9, 9, 0.01)
y = st.norm.pdf(x, 0, 1)

plot(x, y, quantile, Z, "a) mu != 1.5")
print(f"p = {p_value1}")

### b) mu > 1.5
row2 = 1 - ALPHA
quantile2 = st.norm.ppf(row2, 0, 1)
p_value2 = 1 - st.norm.cdf(Z)

plot(x, y, quantile2, Z, "b) mu > 1.5")
print(f"p = {p_value2}")

### c) mu < 1.5
p_value3 = st.norm.cdf(Z)

plot(x, y, quantile2, Z, "c) mu < 1.5")
print(f"p = {p_value3}")