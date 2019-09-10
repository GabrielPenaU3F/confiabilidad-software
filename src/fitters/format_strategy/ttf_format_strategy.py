from src.fitters.format_strategy.format_strategy import FormatStrategy


class TTFFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        super().__init__(data, model)
        self.execute_ml_function = self.model.estimate_ttf_parameters_by_maximum_likelihood

    def fit_model(self, **kwargs):

        end = self.determine_end_sample(kwargs.get('end_sample'))

        initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

        times_from_zero = self.data.get_times()[0:end + 1]
        cumulative_failures = self.data.get_cumulative_failures()[0:end + 1]
        ttf_original_data = self.data.get_data()[0:end]

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times_from_zero, cumulative_failures,
                                                                         initial_approx)
        if kwargs.get('lsq_only') is True:
            ml_params = lsq_params
        else:
            ml_params = self.execute_ml_function(ttf_original_data, lsq_params, solving_method='krylov')

        return lsq_params, ml_params

    def determine_initial_approx(self, initial_approx_arg):
        if initial_approx_arg is not None:
            return initial_approx_arg
        else:
            return self.model.get_default_initial_approx('ttf')

    def calculate_aic(self, *model_parameters):
        original_times = self.data.get_data()
        return self.model.calculate_ttf_aic(original_times, *model_parameters)
