import numpy as np

from src.auxiliar_math.gamma.gamma import lower_incomplete_gamma
from src.domain.saddlepoint_calculators.purebirth_saddlepoint_calculator import PureBirthSaddlepointCalculator


class BarrazaContagionSaddlepointCalculator(PureBirthSaddlepointCalculator):

    def g_second(self, x, k, upper_limit):
        a, b = self.model_parameters
        last_term_num = (a**2)*b*(k-1)*((1+a*x)**(b-2))*(b-1+((1+a*x)**b))
        last_term_den = ((1+a*x)**b - 1)**2
        return (-1/(x**2)) + (a**2 / ((1 + a*x)**2)) - (a**2)*(b-1)*((1+a*x)**(b-2)) - last_term_num/last_term_den

    def g_x(self, x, k, upper_limit):
        lambda_ = self.lambda_function(k, x, *self.model_parameters)
        mu = self.mu_function(x, *self.model_parameters)
        gammainc = lower_incomplete_gamma(upper_limit, k, min_decimals=12)
        return np.log(x) + np.log(lambda_) + (k - 1) * np.log(mu) - mu - np.math.log(gammainc)