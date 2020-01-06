from src.data.data_formater import TTFDataFormater
from src.domain.fitters.format_strategy.format_strategy import FormatStrategy


class TTFFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        data_formater = TTFDataFormater()
        super().__init__(data, model, data_formater)
        self.execute_ml_function = self.model.estimate_ttf_parameters_by_maximum_likelihood

    def determine_ml_function_parameters(self, formated_data, lsq_params):
        return formated_data.get_formated_times(), lsq_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'ttf')

    def calculate_aic(self, *model_parameters):
        original_times = self.data.get_data()
        return self.model.calculate_ttf_aic(original_times, *model_parameters)
