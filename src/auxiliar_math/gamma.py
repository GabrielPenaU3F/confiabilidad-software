import scipy.special as sp


def lower_incomplete_gamma(a, z):
    upper_limit = a
    gamma_variable = z
    normalized_lower_incomplete_gamma = sp.gammainc(gamma_variable, upper_limit)
    gamma_z = sp.gamma(z)
    return gamma_z * normalized_lower_incomplete_gamma
