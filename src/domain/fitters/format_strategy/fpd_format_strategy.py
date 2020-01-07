from src.data.data_formater import FPDDataFormater
from src.domain.fitters.format_strategy.format_strategy import FormatStrategy


class FPDFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        data_formater = FPDDataFormater()
        super().__init__(data, model, data_formater)
        self.execute_ml_function = self.model.estimate_grouped_fpd_parameters_by_maximum_likelihood

    def determine_ml_function_parameters(self, formated_data, lsq_params):
        return formated_data.get_formated_times(), formated_data.get_fpd(), lsq_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'grouped-fpd')

    def calculate_aic(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)
