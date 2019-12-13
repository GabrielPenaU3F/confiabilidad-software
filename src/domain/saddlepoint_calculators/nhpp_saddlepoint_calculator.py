from abc import abstractmethod

import numpy as np

from src.auxiliar_math.gamma.gamma import lower_incomplete_gamma
from src.auxiliar_math.maximum import find_maximum


class NHPPSaddlepointCalculator:

    model_parameters = None

    def __init__(self, mu_function, lambda_function):
        self.lambda_function = lambda_function
        self.mu_function = mu_function

    def calculate_saddlepoint_mttf_approximation(self, k, upper_limit, *model_parameters):
        self.model_parameters = model_parameters
        x0 = find_maximum(self.g_x, 50, k, upper_limit)  # Where the maximum of g(x) is located
        A = 1
        saddlepoint_approximation = \
            self.f_x() * np.exp(A * self.g_x(x0, k, upper_limit)) * \
            np.sqrt(2 * np.pi / (-A * self.g_second(x0, k, upper_limit)))
        return saddlepoint_approximation

    def f_x(self):
        return 1

    def g_x(self, x, k, upper_limit):
        lambda_ = self.lambda_function(x, *self.model_parameters)
        mu = self.mu_function(x, *self.model_parameters)
        gammainc = lower_incomplete_gamma(upper_limit, k, min_decimals=12)
        return np.log(x) + np.log(lambda_) + (k - 1) * np.log(mu) - mu - np.math.log(gammainc)

    # Second derivative of g(x)
    @abstractmethod
    def g_second(self, x, k, upper_limit):
        pass
