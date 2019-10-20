import numpy as np

from src.domain.models.model_estimator import ModelEstimator


class BarrazaContagionEstimator(ModelEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-cumulative': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        parenthesis = 1 + a * t
        sq_brackets = np.power(parenthesis, b) - 1
        return sq_brackets/b

    def calculate_lambda(self, data, *model_parameters):
        a, b = model_parameters
        r, t = data
        numerator = 1 + b * r
        denominator = 1 + a * t
        return a * numerator / denominator

    def calculate_limit_for_mu(self, *model_parameters):
        a, b = model_parameters
        if b > 0:
            return np.inf
        elif b < 0:
            return -1/b

    def ttf_ml_equations(self, times, vec):
        return None

    def grouped_cumulative_ml_equations(self, days, cumulative_failures, vec):
        return None

    def grouped_fpd_ml_equations(self, times, failures_per_day, vec):
        return None