from src.data.data_formater import TTFDataFormater
from src.domain.fitters.format_strategy.format_strategy import FormatStrategy
import numpy as np


class TTFFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        data_formater = TTFDataFormater()
        super().__init__(data, model, data_formater)
        self.execute_ml_function = self.model.estimate_ttf_parameters_by_maximum_likelihood

    def fit_model(self, optional_arguments):

        optional_arguments = self.set_initial_approx(optional_arguments)
        formated_data = self.data_formater.give_format(self.data, optional_arguments)
        ttf = formated_data.get_formated_times()
        original_times = formated_data.get_original_times()
        cumulative_failures = formated_data.get_cumulative_failures()
        initial_approx = optional_arguments.get_initial_approx()

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(
            original_times, cumulative_failures[1:len(cumulative_failures)], initial_approx)
        ml_function_parameters = ttf, lsq_params
        ml_params = self.determine_ml_estimates(optional_arguments.get_lsq_only(), *ml_function_parameters)

        return lsq_params, ml_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'ttf')

    def calculate_aic(self, *model_parameters):
        original_times = self.data.get_data()
        return self.model.calculate_ttf_aic(original_times, *model_parameters)
