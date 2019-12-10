import numpy as np

from src.auxiliar_math.maximum import find_maximum
from src.domain.saddlepoint_calculators.nhpp_saddlepoint_calculator import NHPPSaddlepointCalculator


class DelayedSShapedSaddlepointCalculator(NHPPSaddlepointCalculator):

    def calculate_saddlepoint_mttf_approximation(self, k, upper_limit, *model_parameters):
        super().calculate_saddlepoint_mttf_approximation(k, upper_limit, *model_parameters)
        x0 = find_maximum(self.g_x, 50, k, upper_limit)  # Where the maximum of g(x) is located
        A = 1
        saddlepoint_approximation = \
            self.f_x() * np.exp(A * self.g_x(x0, k, upper_limit)) * \
            np.sqrt(2 * np.pi / (-A * self.g_second(x0, k, upper_limit)))
        return saddlepoint_approximation

    def g_second(self, x, k, upper_limit):
        a, b = self.model_parameters
        quotient = (1 + (b * x - 1) * np.exp(b * x)) / (1 + b * x - np.exp(b * x)) ** 2
        big_brackets = a * np.exp(-b * x) * (b * x - 1) - (k - 1) * quotient
        return (-2 / (x ** 2)) + (b ** 2) * big_brackets
