from src.data.data_formater import FPDDataFormater
from src.domain.fitters.format_strategy.format_strategy import FormatStrategy


class FPDFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        data_formater = FPDDataFormater()
        super().__init__(data, model, data_formater)
        self.execute_ml_function = self.model.estimate_grouped_fpd_parameters_by_maximum_likelihood

    def fit_model(self, optional_arguments):

        optional_arguments = self.set_initial_approx(optional_arguments)
        formated_data = self.data_formater.give_format(self.data, optional_arguments)
        original_times = formated_data.get_original_times()
        formated_times = formated_data.get_formated_times()
        fpd = formated_data.get_fpd()
        cumulative_failures = formated_data.get_cumulative_failures()
        initial_approx = optional_arguments.get_initial_approx()

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(
            original_times, cumulative_failures, initial_approx)
        ml_function_parameters = optional_arguments.get_lsq_only(), formated_times, fpd, lsq_params
        ml_params = self.determine_ml_estimates(*ml_function_parameters)
        return lsq_params, ml_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'grouped-fpd')

    def calculate_aic(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)
