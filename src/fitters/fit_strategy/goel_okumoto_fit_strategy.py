from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = GoelOkumotoEstimator()
        super().__init__(project_name, model)

    def fit_ttf(self):
        self.validate_format(self.data)
        ttf = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()
        ttf_without_zero = ttf[1:]

        initial_approx = (1, 0.5)
        go_lsq_params = self.model.fit_mean_failure_number_by_least_squares(ttf, cumulative_failures, initial_approx)

        go_ml_params = self.model.estimate_ttf_parameters_by_maximum_likelihood(ttf_without_zero,
                                                                                go_lsq_params,
                                                                                solving_method='krylov')

        return go_lsq_params, go_ml_params

    def fit_grouped_cumulative(self):
        pass

    def fit_grouped_fpd(self):
        pass

    def calculate_prr(self):
        pass

    def calculate_aic(self):
        pass

