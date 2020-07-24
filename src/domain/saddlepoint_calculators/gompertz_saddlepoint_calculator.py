import numpy as np

from src.domain.saddlepoint_calculators.purebirth_saddlepoint_calculator import PureBirthSaddlepointCalculator


class GompertzSaddlepointCalculator(PureBirthSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b, c = self.model_parameters
        mu = self.mu_function(x, a, b, c)
        return (-1/(x**2)) - np.log(b) * (np.log(c) ** 2) * (c**x) * (mu - k + mu * (c**x) * np.log(b))
