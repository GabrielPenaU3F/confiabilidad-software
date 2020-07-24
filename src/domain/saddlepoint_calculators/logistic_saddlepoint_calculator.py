import numpy as np

from src.domain.saddlepoint_calculators.purebirth_saddlepoint_calculator import PureBirthSaddlepointCalculator


class LogisticSaddlepointCalculator(PureBirthSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b, c = self.model_parameters
        first_term = 3 + (b**2) * (x**2) * (k + 1) * np.cosh(b * (c - x) / 2)
        second_term = np.cosh((3/2) * b * (c - x))
        third_term = a * (b**2) * (x**2) * np.sinh(b * (c - x) / 2)
        numerator = -2 * np.exp((3 / 2) * b * (c - x)) * (first_term + second_term + third_term)
        denominator = ((np.exp(b * c) + np.exp(b * x)) ** 3) * (x**2)
        return numerator / denominator
