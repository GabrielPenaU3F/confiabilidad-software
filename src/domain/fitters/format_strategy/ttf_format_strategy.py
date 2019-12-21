from src.domain.fitters.format_strategy.format_strategy import FormatStrategy


class TTFFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        super().__init__(data, model)
        self.execute_ml_function = self.model.estimate_ttf_parameters_by_maximum_likelihood

    def fit_model(self, optional_arguments):

        optional_arguments = self.set_initial_approx(optional_arguments)

        end = self.determine_end_sample(optional_arguments.get_end_sample())

        times_from_zero = self.data.get_times()[0:end + 1]
        cumulative_failures = self.data.get_cumulative_failures()[0:end + 1]
        ttf_original_data = self.data.get_data()[0:end]

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times_from_zero, cumulative_failures,
                                                                         optional_arguments)
        ml_function_parameters = ttf_original_data, lsq_params, optional_arguments.get_x0()
        ml_params = self.determine_ml_estimates(optional_arguments.get_lsq_only(), *ml_function_parameters)
        return lsq_params, ml_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'ttf')

    def calculate_aic(self, *model_parameters):
        original_times = self.data.get_data()
        return self.model.calculate_ttf_aic(original_times, *model_parameters)