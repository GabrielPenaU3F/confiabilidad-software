import numpy as np

from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.musa_okumoto_saddlepoint_calculator import MusaOkumotoSaddlepointCalculator


class MusaOkumotoEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }
        self.bounds = ([0, 0], [+np.inf, 1])
        saddlepoint_calculator = MusaOkumotoSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        return a * (np.log(1 + b*t))

    def calculate_lambda(self, t, *model_parameters):
        a, b = model_parameters
        return a * b / (1 + b*t)

    def calculate_limit_for_mu(self, *model_parameters):
        return np.infty

    def ttf_ml_equations(self, times, vec):
        a, b = vec
        return (self.ttf_ml_equation_1(a, b, times),
                self.ttf_ml_equation_2(a, b, times))

    def ttf_ml_equation_1(self, a, b, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        t_n = times[-1]
        return n - (self.calculate_mean(t_n, a, b) - self.calculate_mean(t_0, a, b))

    def ttf_ml_equation_2(self, a, b, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        t_n = times[-1]
        lambda_tn = self.calculate_lambda(t_n, a, b)
        lambda_t0 = self.calculate_lambda(t_0, a, b)
        sum = 0
        for k in range(n):
            t_k = times[k]
            lambda_tk = self.calculate_lambda(t_k, a, b)
            sum += t_k * lambda_tk
        return n - (t_n * lambda_tn - t_0 * lambda_t0) - sum/a

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b = vec
        return (self.grouped_fpd_ml_equation_1(a, b, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, days, failures_per_day):
        deltas_yi = failures_per_day
        sum_delta_yi = np.sum(deltas_yi)
        t_0 = days[0]
        t_n = days[-1]
        mu_t0 = self.calculate_mean(t_0, a, b)
        mu_tn = self.calculate_mean(t_n, a, b)
        return sum_delta_yi - (mu_tn - mu_t0)

    def grouped_fpd_ml_equation_2(self, a, b, days, failures_per_day):
        n = len(days)
        t_0 = days[0]
        t_n = days[-1]
        lambda_t0 = self.calculate_lambda(t_0, a, b)
        lambda_tn = self.calculate_lambda(t_n, a, b)
        deltas_yi = failures_per_day
        sum_delta_x_phi = 0
        for i in range(1, n):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            delta_y_i = deltas_yi[i - 1]
            sum_delta_x_phi += (delta_y_i * self.calculate_phi(a, b, t_i, t_i_minus_1))
        return sum_delta_x_phi - (t_n * lambda_tn - t_0 * lambda_t0)

    def calculate_phi(self, a, b, t_i, t_i_minus_1):
        num = t_i * self.calculate_lambda(t_i, a, b) - t_i_minus_1 * self.calculate_lambda(t_i_minus_1, a, b)
        den = self.calculate_mean(t_i, a, b) - self.calculate_mean(t_i_minus_1, a, b)
        return num/den
