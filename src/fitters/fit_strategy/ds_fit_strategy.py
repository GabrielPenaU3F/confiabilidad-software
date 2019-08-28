import numpy as np

from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator


class DSFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = DelayedSShapedEstimator()
        super().__init__(project_name, model)

    def fit_ttf(self, **kwargs):
        times_from_zero = self.data.get_times()
        ttf_original_data = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()

        if kwargs.keys().__contains__('initial_approx'):
            initial_approx = kwargs.get('initial_approx')
        else:
            initial_approx = (1, 0.5)
        ds_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times_from_zero, cumulative_failures, initial_approx)

        ds_ml_params = self.model.estimate_ttf_parameters_by_maximum_likelihood(ttf_original_data,
                                                                                ds_lsq_params,
                                                                                solving_method='krylov')

        return ds_lsq_params, ds_ml_params

    def fit_grouped_cumulative(self, **kwargs):
        cumulative_failures = self.data.get_cumulative_failures()
        times = np.arange(1, len(cumulative_failures) + 1)

        if kwargs.keys().__contains__('initial_approx'):
            initial_approx = kwargs.get('initial_approx')
        else:
            initial_approx = (1, 0.5)
        ds_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        ds_ml_params = self.model. \
            estimate_grouped_cumulative_parameters_by_maximum_likelihood(times, cumulative_failures, ds_lsq_params,
                                                                         solving_method='krylov')

        return ds_lsq_params, ds_ml_params

    def fit_grouped_fpd(self, **kwargs):
        fpd = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()
        times = np.arange(1, len(fpd) + 1)

        if kwargs.keys().__contains__('initial_approx'):
            initial_approx = kwargs.get('initial_approx')
        else:
            initial_approx = (1, 0.5)
        ds_lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        ds_ml_params = self.model. \
            estimate_grouped_fpd_parameters_by_maximum_likelihood(times, fpd, ds_lsq_params,
                                                                  solving_method='krylov')

        return ds_lsq_params, ds_ml_params
