import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import statistics


f = open("staty.txt", "r")
data = f.read()
lepszedata = sorted(data.split(","))
f.close()


inty_data = [eval(i) for i in lepszedata]

mean = np.mean(inty_data)
std = np.std(inty_data)
norm_cdf = st.norm.cdf(inty_data, mean, std)


"""
#mediana
median = np.median(inty_data)

#kwartyle rzędu 1/4 i 3/4
q1 = np.percentile(inty_data, 25)
q3 = np.percentile(inty_data, 75)

#rozstęp międzykwartylowy
iqr = q3 - q1

#rozstęp
range_ = max(inty_data) - min(inty_data)

#wariancja
variance = np.var(inty_data)

# odchylenie standardowe
std_deviation = np.std(inty_data)

#  współczynnik zmienności
cv = std_deviation / mean

print(median)
print(q1)
print(q3)
print(range_)
print(variance)
print(std_deviation)
print(cv)"""

import matplotlib.pyplot as plt
import numpy as np

klist = np.arange(0,2751,20)
Winsorized = [np.mean(st.mstats.winsorize((inty_data),(k/5534,k/5534))) for k in klist]



# Rysowanie wykresu
plt.scatter(klist, Winsorized, s=3.4, color="#6A9662")
plt.title("Średnia winsorowska w zależności od parametru k")
plt.xlabel("Liczba zamienionych wartości k")
plt.ylabel("Średnia winsorowska")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.yticks(np.arange(22.5, 23.5, 0.1))
plt.show()



"""



inty_data = [int(i) for i in lepszedata]
k_values = np.arange(1, 2751)
trimmed_means = []

for k in k_values:
    trimmed_data = st.trim1(inty_data, proportiontocut=k/len(inty_data))
    trimmed_mean = np.mean(trimmed_data)
    trimmed_means.append(trimmed_mean)

plt.scatter(k_values, trimmed_means, s=0.9, color="#6A9662")
plt.xlabel('Parametr k')
plt.ylabel('Średnia ucinana')
plt.title('Średnia ucinana w zależności od parametru k')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.yticks(np.arange(20, 24, 0.5))
plt.show()"""

"""

### histogram
plt.figure(figsize=(11,7))
plt.hist(inty_data, bins = 33, stacked=True, edgecolor="#6A9662", alpha = 1, color="#DDFFDD", density = "True", label="Gęstość empiryczna")
plt.plot(inty_data, [(1/(std*(np.pi*2)**(0.5)))*np.exp((-(x-mean)**2)/(2*std**2)) for x in inty_data], color = "orange", alpha=0.6, label="Gęstość teoretyczna rozkładu normalnego")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(min(inty_data), max(inty_data), 2))
plt.yticks(np.arange(0, 0.11, 0.01))
plt.axvline(statistics.mode(inty_data), color="red", alpha = 0.7, label="Moda")
plt.title("Gęstość wieków kobiet")
plt.xlabel("Wiek w latach")
plt.ylabel("f(x)")
plt.legend()
plt.show()


### dystrybuanta

emp_cdf = np.linspace(0, 1, len(lepszedata))


plt.figure(figsize=(11,7))
plt.plot(inty_data, emp_cdf, color="#6A9662", label="Dystrybuanta empiryczna")
plt.plot(inty_data, norm_cdf, color="orange", alpha=0.6, label="Dystrybuanta teoretyczna rozkładu normalnego")
plt.title("Dystrybuanta wieków kobiet")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(range(min(inty_data), max(inty_data), 2))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel("Wiek w latach")
plt.ylabel("F(x)")
plt.legend()
plt.show()


###boxplot

plt.figure(figsize=(7, 7))
plt.boxplot(inty_data, vert=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.yticks(range(min(inty_data), max(inty_data)+2, 2))
plt.ylabel("Wiek w latach")
plt.title("Wykres pudełkowy wieków kobiet")
plt.show()


###qqplot

st.probplot(inty_data, dist='norm', sparams=(mean, std), plot=plt)
plt.xlabel('Kwantyle teoretyczne')
plt.ylabel('Kwantyle empiryczne')
plt.title('Wykres kwantylowy')
plt.show()



#średnia arytmetyczna
mean = np.mean(inty_data)

#średnia harmoniczna
harm_mean = len(inty_data) / np.sum(1 / np.array(inty_data))

# średnia geometryczna
geo_mean = np.prod(np.array(inty_data)) ** (1 / len(inty_data))

srgeom = st.gmean(inty_data)

print(f"Średnia arytmetyczna: {mean:.2f}")
print(f"Średnia harmoniczna: {harm_mean:.2f}")
print(f"Średnia geometryczna: {geo_mean:.2f}")
print(srgeom)"""