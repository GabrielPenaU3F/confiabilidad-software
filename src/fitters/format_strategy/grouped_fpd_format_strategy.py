from src.fitters.format_strategy.format_strategy import FormatStrategy


class GroupedFPDFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        super().__init__(data, model)
        self.execute_ml_function = self.model.estimate_grouped_fpd_parameters_by_maximum_likelihood

    def fit_model(self, **kwargs):

        end = self.determine_end_sample(kwargs.get('end_sample'))

        initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

        fpd = self.data.get_data()[0:end]
        cumulative_failures = self.data.get_cumulative_failures()[0:end]
        times = self.data.get_times()[0:end]

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures, initial_approx)
        ml_function_parameters = times, fpd, lsq_params
        ml_params = self.determine_ml_parameters(kwargs.get('lsq_only'), *ml_function_parameters)
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
