from data.data_repository import DataRepository
from src.exceptions.exceptions import NotAdmittedFormatException
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator


class DSFitStrategy(FitStrategy):

    def fit_ttf(self, project_name):
        data = DataRepository.provide_observed_data_from_project(project_name)
        self.validate_format(data)
        ttf = data.get_data()
        cumulative_failures = data.get_cumulative_failures()
        ttf_without_zero = ttf[1:]

        ds = DelayedSShapedEstimator()
        initial_approx = (1, 0.5)
        ds_lsq_params = ds.fit_mean_failure_number_by_least_squares(ttf, cumulative_failures, initial_approx)

        ds_ml_params = ds.estimate_ttf_parameters_by_maximum_likelihood(ttf_without_zero,
                                                                        ds_lsq_params,
                                                                        solving_method='krylov')

        return ds_lsq_params, ds_ml_params

    def fit_grouped_cumulative(self, project_name):
        pass

    def fit_grouped_fpd(self, project_name):
        pass

    def calculate_prr(self, project_name):
        pass

    def calculate_aic(self, project_name):
        pass
