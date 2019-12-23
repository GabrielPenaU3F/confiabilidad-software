import numpy as np

from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.gompertz_saddlepoint_calculator import GompertzSaddlepointCalculator


class GompertzEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (25, 0.5, 0.5),
            'grouped-fpd': (250, 0.5, 0.5)
        }
        saddlepoint_calculator = GompertzSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b, c = model_parameters
        return a * (b ** (c ** t))

    def calculate_lambda(self, t, *model_parameters):
        a, b, c = model_parameters
        return a * (c ** t) * (b ** (c ** t)) * np.log(b) * np.log(c)

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
        t_n = times[-1]
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return n - (mu_tn - mu_t0)

    def ttf_ml_equation_2(self, a, b, c, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        logb = np.log(b)
        logc = np.log(c)
        t_n = times[-1]
        lambda_t0 = self.calculate_lambda(t_0, a, b, c)
        lambda_tn = self.calculate_lambda(t_n, a, b, c)
        sum_second_term = 0
        for k in range(n):
            sum_second_term += (c ** times[k])
        third_term = (lambda_tn - lambda_t0)/logc
        return n + logb * sum_second_term - third_term

    def ttf_ml_equation_3(self, a, b, c, times):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        logb = np.log(b)
        logc = np.log(c)
        t_n = times[-1]
        lambda_t0 = self.calculate_lambda(t_0, a, b, c)
        lambda_tn = self.calculate_lambda(t_n, a, b, c)
        sum_second_term = 0
        for k in range(n):
            tk = times[k]
            c_pow_tk = (c ** tk)
            sum_second_term += (tk * (1 + c_pow_tk * logb))
        third_term = t_n * lambda_tn - t_0 * lambda_t0
        return n + logc * sum_second_term - third_term

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b, c = vec
        return (self.grouped_fpd_ml_equation_1(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_3(a, b, c, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, c, days, failures_per_day):
        t_0, days = self.separate_time_data(days)
        deltas_yi = failures_per_day
        sum_deltas_yi = np.sum(deltas_yi)
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return sum_deltas_yi - (mu_tn - mu_t0)

    def grouped_fpd_ml_equation_2(self, a, b, c, days, failures_per_day):
        n = len(days)
        deltas_yi = failures_per_day
        t_0 = days[0]
        phi_t0 = self.calculate_phi(t_0, b, c)
        t_n = days[-1]
        phi_tn = self.calculate_phi(t_n, b, c)
        sum_first_term = 0
        for i in range(1, n):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            phi_ti = self.calculate_phi(t_i, b, c)
            phi_ti_minus_1 = self.calculate_phi(t_i_minus_1, b, c)
            delta_y_i = deltas_yi[i - 1]
            sum_first_term += delta_y_i * (phi_ti - phi_ti_minus_1) / (mu_ti - mu_ti_minus_1)
        return sum_first_term - (phi_tn - phi_t0)

    def grouped_fpd_ml_equation_3(self, a, b, c, days, failures_per_day):
        n = len(days)
        deltas_yi = failures_per_day
        t_0 = days[0]
        psi_t0 = self.calculate_psi(t_0, b, c)
        t_n = days[-1]
        psi_tn = self.calculate_psi(t_n, b, c)
        sum_first_term = 0
        for i in range(1, n):
            t_i = days[i]
            t_i_minus_1 = days[i - 1]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            psi_ti = self.calculate_psi(t_i, b, c)
            psi_ti_minus_1 = self.calculate_psi(t_i_minus_1, b, c)
            delta_y_i = deltas_yi[i - 1]
            sum_first_term += delta_y_i * (psi_ti - psi_ti_minus_1) / (mu_ti - mu_ti_minus_1)
        return sum_first_term - (psi_tn - psi_t0)

    def calculate_phi(self, t, b, c):
        return (b ** ((c ** t) - 1)) * (c ** t)

    def calculate_psi(self, t, b, c):
        return t * (b ** (c ** t)) * (c ** (t - 1))







