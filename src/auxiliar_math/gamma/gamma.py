import scipy.special as sp
import numpy as np

from src.auxiliar_math.gamma.gamma_strategy import ExactGammaStrategy, LargeKApproximationGammaStrategy


def lower_incomplete_gamma(a, k, **kwargs):
    min_decimals = kwargs.get('min_decimals')
    upper_limit = a
    gamma_k_strategy = choose_gamma_strategy(k, min_decimals)
    gamma_k = gamma_k_strategy.get_gamma()
    if np.isinf(upper_limit):
        return gamma_k
    return gamma_k_strategy.lower_incomplete_gamma(upper_limit)


def choose_gamma_strategy(k, min_decimals):
    if k < 50:
        return ExactGammaStrategy(k, min_decimals)
    else:
        return LargeKApproximationGammaStrategy(k, min_decimals)
