import numpy as np

from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = GoelOkumotoEstimator()
        super().__init__(project_name, model)

    def fit_ttf(self):
        times_from_zero = self.data.get_times()
        ttf_original_data = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()

        initial_approx = (1, 0.5)
        go_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times_from_zero, cumulative_failures, initial_approx)

        go_ml_params = self.model.estimate_ttf_parameters_by_maximum_likelihood(ttf_original_data,
                                                                                go_lsq_params,
                                                                                solving_method='krylov')

        return go_lsq_params, go_ml_params

    def fit_grouped_cumulative(self):
        cumulative_failures = self.data.get_cumulative_failures()
        times = np.arange(1, len(cumulative_failures) + 1)

        initial_approx = (1, 0.5)
        go_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        go_ml_params = self.model. \
            estimate_grouped_cumulative_parameters_by_maximum_likelihood(times, cumulative_failures, go_lsq_params,
                                                                         solving_method='krylov')

        return go_lsq_params, go_ml_params

    def fit_grouped_fpd(self):
        fpd = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()
        times = np.arange(1, len(fpd) + 1)

        initial_approx = (1, 0.5)
        go_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        go_ml_params = self.model. \
            estimate_grouped_fpd_parameters_by_maximum_likelihood(times, fpd, go_lsq_params,
                                                                  solving_method='krylov')

        return go_lsq_params, go_ml_params

