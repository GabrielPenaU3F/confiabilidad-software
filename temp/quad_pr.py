import numpy as np
import scipy.integrate

from src.auxiliar_math import gamma


def calculate_mean(t, a, b):
    return a * (1 - (1 + b * t) * np.exp(-b * t))


def calculate_lambda(t, a, b):
    return a * (b ** 2) * t * np.exp(-b * t)


def integrand_u(u, k, a, b):
    return u * calculate_lambda(u, a, b) * (calculate_mean(u, a, b) ** (k - 1)) * np.exp(-calculate_mean(u, a, b))


a = 893.6388827658578
b = 0.02178799631089532
upper_limit = a
k = 106

denominator = gamma.lower_incomplete_gamma(upper_limit, 200)
numerator = scipy.integrate.quad(lambda u: integrand_u(u, k, a, b)/denominator, 0, +np.inf, limit=2000)[0]
print(numerator)
