import numpy as np

from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.logistic.logistic_estimator import LogisticEstimator


class LogisticFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = LogisticEstimator()
        super().__init__(project_name, model)

    def fit_ttf(self):
        ttf = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()
        ttf_without_zero = ttf[1:]

        initial_approx = (10, 0.05, 20)
        log_lsq_params = self.model.fit_mean_failure_number_by_least_squares(ttf, cumulative_failures, initial_approx)

        log_ml_params = self.model.estimate_ttf_parameters_by_maximum_likelihood(ttf_without_zero,
                                                                                 log_lsq_params,
                                                                                 solving_method='krylov')

        return log_lsq_params, log_ml_params

    def fit_grouped_cumulative(self):
        cumulative_failures = self.data.get_cumulative_failures()
        times = np.arange(1, len(cumulative_failures) + 1)

        initial_approx = (10, 0.05, 20)
        log_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        log_ml_params = self.model. \
            estimate_grouped_cumulative_parameters_by_maximum_likelihood(times, cumulative_failures, log_lsq_params,
                                                                         solving_method='krylov')

        return log_lsq_params, log_ml_params

    def fit_grouped_fpd(self):
        pass
