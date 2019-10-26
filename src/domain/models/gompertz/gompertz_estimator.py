import numpy as np

from src.domain.models.model_estimator import ModelEstimator


class GompertzEstimator(ModelEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (0.5, 0.5, 0.5),
            'grouped-cumulative': (0.5, 0.5, 0.5),
            'grouped-fpd': (0.5, 0.5, 0.5)
        }

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
        pass

    def ttf_ml_equation_2(self, a, b, c, times):
        pass

    def ttf_ml_equation_3(self, a, b, c, times):
        pass

    def grouped_cumulative_ml_equations(self, days, cumulative_failures, vec):
        a, b, c = vec
        return (self.grouped_cumulative_ml_equation_1(a, b, c, days, cumulative_failures),
                self.grouped_cumulative_ml_equation_2(a, b, c, days, cumulative_failures),
                self.grouped_cumulative_ml_equation_3(a, b, c, days, cumulative_failures))

    def grouped_cumulative_ml_equation_1(self, a, b, c, days, cumulative_failures):
        pass

    def grouped_cumulative_ml_equation_2(self, a, b, c, days, cumulative_failures):
        pass

    def grouped_cumulative_ml_equation_3(self, a, b, c, days, cumulative_failures):
        pass

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b, c = vec
        return (self.grouped_fpd_ml_equation_1(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_3(a, b, c, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, c, days, failures_per_day):
        pass

    def grouped_fpd_ml_equation_2(self, a, b, c, days, failures_per_day):
        pass

    def grouped_fpd_ml_equation_3(self, a, b, c, days, failures_per_day):
        pass








