import numpy as np


from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.logistic_saddlepoint_calculator import LogisticSaddlepointCalculator


class LogisticEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (10, 0.05, 20),
            'grouped-fpd': (0.01, 0.001, 0.00001)
        }
        self.bounds = ([0, 0, 0], [+np.inf, 1, +np.inf])
        saddlepoint_calculator = LogisticSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b, c = model_parameters
        return a / (1 + self.calculate_phi(b, c, t))

    def calculate_lambda(self, t, *model_parameters):
        a, b, c = model_parameters
        phi = self.calculate_phi(b, c, t)
        numerator = a * b * phi
        denominator = (1 + phi)**2
        return numerator/denominator

    def calculate_limit_for_mu(self, *model_parameters):
        a, b, c = model_parameters
        return a

    def ttf_ml_equations(self, times, vec):
        a, b, c = vec
        return (self.ttf_ml_equation_1(a, b, c, times),
                self.ttf_ml_equation_2(a, b, c, times),
                self.ttf_ml_equation_3(a, b, c, times))

    def ttf_ml_equation_1(self, a, b, c, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return n - (mu_tn - mu_t0)

    def ttf_ml_equation_2(self, a, b, c, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        sum_tk = np.sum(times)
        fourth_term_sum = 0
        for k in range(n):
            t_k = times[k]
            psi_tk = self.calculate_psi(b, c, t_k)
            mu_tk = self.calculate_mean(t_k, a, b, c)
            fourth_term_sum += (psi_tk * mu_tk)
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        psi_t0 = self.calculate_psi(b, c, t_0)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        psi_tn = self.calculate_psi(b, c, t_n)
        fifth_term = (mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0

        return n/b + sum_tk - n * c + (2/a) * fourth_term_sum + (1/a) * fifth_term

    def ttf_ml_equation_3(self, a, b, c, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        second_term_sum = 0
        for k in range(n):
            t_k = times[k]
            mu_tk = self.calculate_mean(t_k, a, b, c)
            phi_tk = self.calculate_phi(t_k, b, c)
            second_term_sum += mu_tk * phi_tk
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        phi_t0 = self.calculate_phi(b, c, t_0)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        phi_tn = self.calculate_phi(b, c, t_n)
        fifth_term = (mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0

        return n * a - 2 * second_term_sum - fifth_term

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b, c = vec
        return (self.grouped_fpd_ml_equation_1(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_3(a, b, c, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, c, days, failures_per_day):
        t_0, days = self.separate_time_data(days)
        deltas_yi = failures_per_day
        sum_delta_yi = np.sum(deltas_yi)
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return sum_delta_yi - (mu_tn - mu_t0)

    def grouped_fpd_ml_equation_2(self, a, b, c, days, failures_per_day):
        t_0, days = self.separate_time_data(days)
        n = len(days)
        deltas_yi = failures_per_day
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        psi_t0 = self.calculate_psi(b, c, t_0)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        psi_tn = self.calculate_psi(b, c, t_n)
        sum = 0
        for i in range(1, n):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            delta_y_i = deltas_yi[i - 1]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            psi_ti = self.calculate_psi(b, c, t_i)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            psi_ti_minus_1 = self.calculate_psi(b, c, t_i_minus_1)
            numerator = (mu_ti**2) * psi_ti - (mu_ti_minus_1**2) * psi_ti_minus_1
            denominator = mu_ti - mu_ti_minus_1
            sum += delta_y_i * numerator / denominator
        return sum - ((mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0)

    def grouped_fpd_ml_equation_3(self, a, b, c, days, failures_per_day):
        t_0, days = self.separate_time_data(days)
        n = len(days)
        deltas_yi = failures_per_day
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        phi_t0 = self.calculate_phi(b, c, t_0)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        phi_tn = self.calculate_phi(b, c, t_n)
        sum = 0
        for i in range(1, n):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            delta_y_i = deltas_yi[i - 1]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            phi_ti = self.calculate_phi(b, c, t_i)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            phi_ti_minus_1 = self.calculate_phi(b, c, t_i_minus_1)
            numerator = -(mu_ti**2) * phi_ti + (mu_ti_minus_1**2) * phi_ti_minus_1
            denominator = mu_ti - mu_ti_minus_1
            sum += delta_y_i * numerator / denominator
        return sum - ((mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0)

    def calculate_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calculate_psi(self, b, c, t):
        return (t - c) * self.calculate_phi(b, c, t)








