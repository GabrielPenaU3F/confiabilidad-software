import numpy as np

from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.delayed_s_shaped_saddlepoint_calculator import \
    DelayedSShapedSaddlepointCalculator


class DelayedSShapedEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-cumulative': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }
        saddlepoint_calculator = DelayedSShapedSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        return a * (1 - (1 + b*t) * self.calculate_exp_minus_bt(b, t))

    def calculate_lambda(self, t, *model_parameters):
        a, b = model_parameters
        return a * (b**2) * t * self.calculate_exp_minus_bt(b, t)

    def calculate_limit_for_mu(self, *model_parameters):
        a, b = model_parameters
        return a

    def ttf_ml_equations(self, times, vec):
        a, b = vec
        return (self.ttf_ml_equation_1(a, b, times),
                self.ttf_ml_equation_2(a, b, times))

    def ttf_ml_equation_1(self, a, b, times):
        n = len(times) - 1
        t_0 = times[0]
        t_n = times[-1]
        mu_t0 = self.calculate_mean(t_0, a, b)
        mu_tn = self.calculate_mean(t_n, a, b)
        return n - (mu_tn - mu_t0)

    def ttf_ml_equation_2(self, a, b, times):
        n = len(times) - 1
        sum_tk = np.sum(times[1:len(times)])
        t_0 = times[0]
        t_n = times[-1]
        psi_tn_t0 = self.calculate_psi(b, t_n, t_0)
        return (2*n/b) - sum_tk - a * b * psi_tn_t0

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b = vec
        return (self.grouped_fpd_ml_equation_1(a, b, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, days, failures_per_day):
        deltas_yi = failures_per_day
        sum_delta_yi = np.sum(deltas_yi)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b)
        return sum_delta_yi - mu_tn

    def grouped_fpd_ml_equation_2(self, a, b, days, failures_per_day):
        deltas_yi = failures_per_day
        sum = 0
        for i in range (len(days)):
            t_i = days[i]
            if i == 0:
                t_i_minus_1 = 0
            else:
                t_i_minus_1 = days[i - 1]
            delta_yi = deltas_yi[i]
            sum += delta_yi * self.calculate_psi(b, t_i, t_i_minus_1) / self.calculate_phi(b, t_i, t_i_minus_1)
        t_n = days[-1]
        return b * sum - a * (1 + b * (t_n**2) * self.calculate_exp_minus_bt(b, t_n))

    def calculate_exp_minus_bt(self, b, t):
        return np.exp(-b * t)

    def calculate_phi(self, b, t_1, t_2):
        first_term = self.calculate_zeta(b, t_2)
        second_term = self.calculate_zeta(b, t_1)
        return first_term - second_term

    def calculate_psi(self, b, t_1, t_2):
        first_term = (t_1**2) * self.calculate_exp_minus_bt(b, t_1)
        second_term = (t_2**2) * self.calculate_exp_minus_bt(b, t_2)
        return first_term - second_term

    def calculate_zeta(self, b, t):
        return (1 + b*t) * self.calculate_exp_minus_bt(b, t)

