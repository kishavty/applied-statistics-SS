import numpy as np
import scipy.stats as st

ns = [20, 50, 100]
mi = 2.1
s = 0.2
alfa = 0.02


def func1():

    count = [0, 0, 0]
    for MCS in range(1, 1001):
        i = 0
        for n in ns:
            data = np.random.normal(mi, s, n)
            
            sr = np.mean(data)
            val_min = sr - st.norm.ppf(1 - alfa/2) * s / np.sqrt(n)
            val_max = sr + st.norm.ppf(1 - alfa/2) * s / np.sqrt(n)
            
            if val_min < mi and mi < val_max:
                count[i] += 1
            i += 1
        
    pp = np.array(count) / 1000
    return pp

result1 = func1()
#prawdopodobienstwo trafienia mi w przedzial ufności dla znanej sigmy
print("sigma znana")
print(f"n = 20: {result1[0]}")
print(f"n = 50: {result1[1]}")
print(f"n = 100: {result1[2]}")



def func2():

    count = [0, 0, 0]
    for MCS in range(1, 1001):
        i = 0
        for n in ns:
            data = np.random.normal(mi, s, n)
            
            sr = np.mean(data)
            odch = np.std(data, ddof=1) 
            val_min = sr - st.t.ppf(1 - alfa/2, n-1) * odch / np.sqrt(n) #test t-studenta
            val_max = sr + st.t.ppf(1 - alfa/2, n-1) * odch / np.sqrt(n)
            
            if val_min < mi and mi < val_max:
                count[i] += 1
            i += 1
        
    pp = np.array(count) / 1000
    return pp

result2 = func2()
#prawdopodobienstwo trafienia mi w przedzial ufności dla nieznanej sigmy
print("sigma nieznana")
print(f"n = 20: {result2[0]}")
print(f"n = 50: {result2[1]}")
print(f"n = 100: {result2[2]}")



