import numpy as np
from scipy.stats import gamma

# Znane parametry rozkładu Gamma
true_shape = 2
true_scale = 3

# Generowanie próbki rozkładu Gamma o znanych parametrach
sample = gamma.rvs(a=true_shape, scale=true_scale, size=1000)

# Obliczanie estymatorów momentowych
sample_mean = np.mean(sample)
sample_variance = np.var(sample)

# Obliczanie estymatorów parametrów
shape_hat = (sample_mean / sample_variance)
scale_hat = (sample_variance / sample_mean)

# Wartości rzeczywiste parametrów
true_parameters = [true_shape, true_scale]

# Wartości estymatorów parametrów
estimated_parameters = [shape_hat, scale_hat]

# Obliczanie błędów estymacji
estimation_errors = np.abs(np.array(true_parameters) - np.array(estimated_parameters))

print("True Parameters:", true_parameters)
print("Estimated Parameters:", estimated_parameters)
print("Estimation Errors:", estimation_errors)
