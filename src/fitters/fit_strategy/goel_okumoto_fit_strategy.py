from datos.repositorio_datos import DataRepository
from src.exceptions.exceptions import NotAdmittedFormatException
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoFitStrategy(FitStrategy):

    def fit_ttf(self, project_name, data):
        data = DataRepository.provide_observed_data_from_project(project_name)
        self.validate_format(data)
        ttf = data.get_data()
        cumulative_failures = data.get_cumulative_failures()
        ttf_without_zero = ttf[1:]

        go = GoelOkumotoEstimator()
        initial_approx = (1, 0.5)
        go_lsq_params = go.fit_mean_failure_number_by_least_squares(ttf, cumulative_failures, initial_approx)

        go_ml_params = go.estimate_ttf_parameters_by_maximum_likelihood(ttf_without_zero,
                                                                        go_lsq_params,
                                                                        solving_method='krylov')

        return go_lsq_params, go_ml_params

    def fit_grouped_cumulative(self, project_name, data):
        pass

    def fit_grouped_fpd(self, project_name, data):
        pass

