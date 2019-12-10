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
        return np.log(x) + np.log(self.lambda_ds_function(x, *self.model_parameters)) + \
               (k - 1) * np.log(self.mu_ds_function(x, *self.model_parameters)) - \
               self.mu_ds_function(x, *self.model_parameters) - \
               np.math.log(lower_incomplete_gamma(upper_limit, k))

    # Second derivative of g(x)
    @abstractmethod
    def g_second(self, x, k, upper_limit):
        pass
