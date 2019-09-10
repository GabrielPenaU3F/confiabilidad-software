import numpy as np

from src.fitters.format_strategy.format_strategy import FormatStrategy


class GroupedCumulativeFormatStrategy(FormatStrategy):

    def fit_model(self, **kwargs):

        end = self.determine_end_sample(kwargs.get('end_sample'))

        initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

        cumulative_failures = self.data.get_cumulative_failures()[0:end]
        times = self.data.get_times()[0:end]
        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        ml_params = self.model. \
            estimate_grouped_cumulative_parameters_by_maximum_likelihood(times, cumulative_failures, lsq_params,
                                                                         solving_method='krylov')

        return lsq_params, ml_params

    def determine_initial_approx(self, initial_approx_arg):
        if initial_approx_arg is not None:
            return initial_approx_arg
        else:
            return self.model.get_default_initial_approx('grouped-cumulative')

    def calculate_aic(self, *model_parameters):
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_aic_grouped_cumulative(cumulative_failures, *model_parameters)
