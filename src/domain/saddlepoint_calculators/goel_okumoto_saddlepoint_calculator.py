import numpy as np

from src.domain.saddlepoint_calculators.nhpp_saddlepoint_calculator import NHPPSaddlepointCalculator


class GoelOkumotoSaddlepointCalculator(NHPPSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b = self.model_parameters
        e_minus_bx = np.exp(-b * x)
        numerator = (k - 1) * (b**2) * e_minus_bx
        denominator = (1 - e_minus_bx)**2
        second_term_quotient = numerator/denominator
        return -1/(x**2) - second_term_quotient + a * (b**2) * e_minus_bx
