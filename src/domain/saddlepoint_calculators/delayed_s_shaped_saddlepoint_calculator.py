import numpy as np

from src.domain.saddlepoint_calculators.nhpp_saddlepoint_calculator import NHPPSaddlepointCalculator


class DelayedSShapedSaddlepointCalculator(NHPPSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b = self.model_parameters
        quotient = (1 + (b * x - 1) * np.exp(b * x)) / (1 + b * x - np.exp(b * x)) ** 2
        big_brackets = a * np.exp(-b * x) * (b * x - 1) - (k - 1) * quotient
        return (-2 / (x ** 2)) + (b ** 2) * big_brackets
