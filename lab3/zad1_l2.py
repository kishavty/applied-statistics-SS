import numpy as np

#próba z rozkładu normalnego o średniej = 2 i odchyleniu standardowym = 2
mu = 2
sigma = 2
sample_size = 2000
sample = np.random.normal(mu, sigma, sample_size)

mediana = np.median(sample)

q1 = np.percentile(sample, 25)
q3 = np.percentile(sample, 75)

#rozstęp z próby
range_sample = np.max(sample) - np.min(sample)
#rozstep miedzykwartylowy
iqr = q3 - q1

#wariancja z próby
variance_sample = np.var(sample, ddof=1)

#dchylenie standardowe
standard_deviation = np.std(sample, ddof=1)

print("Mediana:", mediana)
print("kwartyl 0.25:", q1)
print("kwartyl 0.75:", q3)
print("Rozstęp z próby:", range_sample)
print("Rozstęp międzykwartylowy:", iqr)
print("Wariancja z próby:", variance_sample)
print("Odchylenie standardowe:", standard_deviation)