import numpy as np

from src.domain.models.model_estimator import ModelEstimator


class GoelOkumotoEstimator(ModelEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-cumulative': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        return a * (1 - self.calculate_exp_minus_bt(b, t))

    def calculate_lambda(self, t, *model_parameters):
        a, b = model_parameters
        return a * b * self.calculate_exp_minus_bt(b, t)

    def ttf_ml_equations(self, times, vec):
        a, b = vec
        return (self.ttf_ml_equation_1(a, b, times),
                self.ttf_ml_equation_2(a, b, times))

    def ttf_ml_equation_1(self, a, b, times):
        n = len(times)
        t_n = times[-1]
        return self.calculate_mean(t_n, a, b) - n

    def ttf_ml_equation_2(self, a, b, times):
        n = len(times)
        t_n = times[-1]
        sum_tk = np.sum(times)
        return sum_tk + a * t_n * self.calculate_exp_minus_bt(b, t_n) - (n / b)

    def grouped_cumulative_ml_equations(self, days, cumulative_failures, vec):
        a, b = vec
        return (self.grouped_cumulative_ml_equation_1(a, b, days, cumulative_failures),
                self.grouped_cumulative_ml_equation_2(a, b, days, cumulative_failures))

    def grouped_cumulative_ml_equation_1(self, a, b, days, cumulative_failures):
        n = len(days)
        sum_yi = np.sum(cumulative_failures)
        sum_exp = 0
        for i in range(len(days)):
            t_i = days[i]
            sum_exp += self.calculate_exp_minus_bt(b, t_i)
        return (sum_yi/a) - n + sum_exp

    def grouped_cumulative_ml_equation_2(self, a, b, days, cumulative_failures):
        sum = 0
        for i in range(len(days)):
            t_i = days[i]
            exp_b_ti = self.calculate_exp_minus_bt(b, t_i)
            parentheses_factor = (cumulative_failures[i] / (1 - exp_b_ti)) - a
            sum += t_i * exp_b_ti * parentheses_factor
        return sum

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b = vec
        return (self.grouped_fpd_ml_equation_1(a, b, days, failures_per_day),
                self.ecuacion_mv_2_fallas_por_dia(a, b, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        suma_delta_yi = np.sum(deltas_yi)
        t_n = dias[-1]
        return suma_delta_yi - self.calculate_mean(t_n, a, b)

    def ecuacion_mv_2_fallas_por_dia(self, a, b, days, failures_per_day):
        t_n = days[-1]
        deltas_yi = failures_per_day
        sum_delta_x_phi = 0
        for i in range(len(days)):
            t_i = days[i]
            if i == 0:
                t_i_minus_1 = 0
            else:
                t_i_minus_1 = days[i - 1]
            sum_delta_x_phi += (deltas_yi[i] * self.calculate_phi(b, t_i, t_i_minus_1))
        return sum_delta_x_phi + a * t_n * self.calculate_exp_minus_bt(b, t_n)

    def calculate_phi(self, b, t_i, t_i_minus_1):
        num = t_i_minus_1 * self.calculate_exp_minus_bt(b, t_i_minus_1) - t_i * self.calculate_exp_minus_bt(b, t_i)
        den = self.calculate_exp_minus_bt(b, t_i_minus_1) - self.calculate_exp_minus_bt(b, t_i)
        return num/den

    def calculate_exp_minus_bt(self, b, t):
        return np.exp(-b * t)







