import numpy as np

from src.domain.saddlepoint_calculators.nhpp_saddlepoint_calculator import NHPPSaddlepointCalculator


class MusaOkumotoSaddlepointCalculator(NHPPSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b = self.model_parameters
        numerator = -(k - 1) * (b**2) * (x**2) * (1 + np.log(1 + b*x)) \
                    + (-1 + b*x * (-2 + a*b*x)) * ((np.log(1 + b*x))**2)
        denominator = (x**2) * ((1 + b*x)**2) * ((np.log(1+ b*x))**2)
        return numerator/denominator