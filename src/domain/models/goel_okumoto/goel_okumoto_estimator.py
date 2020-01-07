import numpy as np

from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.goel_okumoto_saddlepoint_calculator import GoelOkumotoSaddlepointCalculator


class GoelOkumotoEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }
        self.bounds = (0, [+np.inf, 1])
        saddlepoint_calculator = GoelOkumotoSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        return a * (1 - self.calculate_exp_minus_bt(b, t))

    def calculate_lambda(self, t, *model_parameters):
        a, b = model_parameters
        return a * b * self.calculate_exp_minus_bt(b, t)

    def calculate_limit_for_mu(self, *model_parameters):
        a, b = model_parameters
        return a

    def ttf_ml_equations(self, times, vec):
        a, b = vec
        return (self.ttf_ml_equation_1(a, b, times),
                self.ttf_ml_equation_2(a, b, times))

    def ttf_ml_equation_1(self, a, b, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        mu_t0 = self.calculate_mean(t_0, a, b)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b)
        return n - (mu_tn - mu_t0)

    def ttf_ml_equation_2(self, a, b, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        t_n = times[-1]
        sum_tk = np.sum(times)
        zeta_tn_t0 = self.calculate_zeta(b, t_n, t_0)
        return -sum_tk - a * zeta_tn_t0 + n/b

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b = vec
        return (self.grouped_fpd_ml_equation_1(a, b, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, days, failures_per_day):
        t_0, days = self.separate_time_data(days)
        deltas_yi = failures_per_day
        sum_delta_yi = np.sum(deltas_yi)
        mu_t0 = self.calculate_mean(t_0, a, b)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b)
        return sum_delta_yi - (mu_tn - mu_t0)

    def grouped_fpd_ml_equation_2(self, a, b, days, failures_per_day):
        n = len(days) - 1
        t_0 = days[0]
        t_n = days[-1]
        deltas_yi = failures_per_day
        sum_delta_x_phi = 0
        for i in range(1, n + 1):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            delta_y_i = deltas_yi[i - 1]
            sum_delta_x_phi += (delta_y_i * self.calculate_phi(a, b, t_i, t_i_minus_1))
        zeta_tn_t0 = self.calculate_zeta(b, t_n, t_0)
        return sum_delta_x_phi - zeta_tn_t0

    def calculate_zeta(self, b, t_1, t_2):
        return t_1 * self.calculate_exp_minus_bt(b, t_1) - t_2 * self.calculate_exp_minus_bt(b, t_2)

    def calculate_phi(self, a, b, t_1, t_2):
        num = self.calculate_zeta(b, t_1, t_2)
        den = self.calculate_mean(t_1, a, b) - self.calculate_mean(t_2, a, b)
        return num/den

    def calculate_exp_minus_bt(self, b, t):
        return np.exp(-b * t)








