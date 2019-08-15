from datos.repositorio_datos import DataRepository
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.models.logistic.logistic_estimator import LogisticEstimator


class LogisticFitStrategy(FitStrategy):

    def fit_ttf(self, project_name, data):
        data = DataRepository.provide_observed_data_from_project(project_name)
        self.validate_format(data)
        ttf = data.get_data()
        cumulative_failures = data.get_cumulative_failures()
        ttf_without_zero = ttf[1:]

        log = LogisticEstimator()
        initial_approx = (10, 0.05, 20)
        log_lsq_params = log.fit_mean_failure_number_by_least_squares(ttf, cumulative_failures, initial_approx)

        log_ml_params = log.estimate_ttf_parameters_by_maximum_likelihood(ttf_without_zero,
                                                                          log_lsq_params,
                                                                          solving_method='krylov')

        return log_lsq_params, log_ml_params

    def fit_grouped_cumulative(self, project_name, data):
        pass

    def fit_grouped_fpd(self, project_name, data):
        pass

