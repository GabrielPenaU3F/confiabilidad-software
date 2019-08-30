import numpy as np

from src.fitters.format_strategy.format_strategy import FormatStrategy


class GroupedFPDFormatStrategy(FormatStrategy):

    def fit_model(self, **kwargs):

        if kwargs.keys().__contains__('end_sample'):
            end = kwargs.get('end_sample')
        else:
            end = len(self.data.get_times())

        initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

        fpd = self.data.get_data()[0:end]
        cumulative_failures = self.data.get_cumulative_failures()[0:end]
        times = np.arange(1, len(fpd) + 1)

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        ml_params = self.model. \
            estimate_grouped_fpd_parameters_by_maximum_likelihood(times, fpd, lsq_params,
                                                                  solving_method='krylov')

        return lsq_params, ml_params

    def determine_initial_approx(self, initial_approx_arg):
        if initial_approx_arg is not None:
            return initial_approx_arg
        else:
            return self.model.get_default_initial_approx('grouped-fpd')

    def calculate_aic(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)

    def calculate_aic_grouped_cumulative(self, *model_parameters):
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_aic_grouped_cumulative(cumulative_failures, *model_parameters)
