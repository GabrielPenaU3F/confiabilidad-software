from abc import ABC, abstractmethod

import numpy as np

from src.auxiliar_math.gamma import lower_incomplete_gamma


class NHPPSaddlepointCalculator(ABC):

    model_parameters = None

    def __init__(self, mu_ds_function, lambda_ds_function):
        self.lambda_ds_function = lambda_ds_function
        self.mu_ds_function = mu_ds_function

    @abstractmethod
    def calculate_saddlepoint_mttf_approximation(self, k, upper_limit, *model_parameters):
        self.model_parameters = model_parameters

    def f_x(self):
        return 1

    def g_x(self, x, k, upper_limit):
        lambda_ds = self.lambda_ds_function(x, *self.model_parameters)
        mu_ds = self.mu_ds_function(x, *self.model_parameters)
        gammainc = lower_incomplete_gamma(upper_limit, k)
        return np.log(x) + np.log(lambda_ds) + (k - 1) * np.log(mu_ds) - mu_ds - np.math.log(gammainc)

    # Second derivative of g(x)
    @abstractmethod
    def g_second(self, x, k, upper_limit):
        pass
