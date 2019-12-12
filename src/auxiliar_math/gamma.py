import scipy.special as sp
import numpy as np


def lower_incomplete_gamma(a, z, **kwargs):
    min_decimals = kwargs.get('min_decimals')
    if min_decimals is not None:
        augmenting_factor = 10**min_decimals
    else:
        augmenting_factor = 100000
    upper_limit = a
    gamma_variable = z
    normalized_lower_incomplete_gamma = sp.gammainc(gamma_variable, upper_limit)
    if z < 50:
        gamma_z = sp.gamma(z)
        if np.isinf(upper_limit):
            return gamma_z
        else:
            return gamma_z * normalized_lower_incomplete_gamma

    else:  # For large z, we take the factorial approximation
        gamma_z = np.math.factorial(np.math.floor(z-1))
        if np.isinf(upper_limit):
            return gamma_z
        else:
            normalized_lower_incomplete_gamma_augmented = int(normalized_lower_incomplete_gamma * augmenting_factor)
            return np.floor_divide(gamma_z * normalized_lower_incomplete_gamma_augmented, augmenting_factor)
