from src.exceptions.exceptions import InvalidArgumentException
from src.fitters.format_strategy.format_strategy import FormatStrategy


class FPDFormatStrategy(FormatStrategy):

    def calculate_aic(self, *model_parameters, **kwargs):
        if len(kwargs) > 1:
            raise InvalidArgumentException("The Grouped Data format does not allow more than 1 optional arguments")
        cumulative_flag = kwargs.get('cumulative')
        if cumulative_flag is True:
            return self.calculate_aic_grouped_cumulative(*model_parameters)
        else:
            return self.calculate_aic_grouped_fpd(*model_parameters)

    def calculate_aic_grouped_cumulative(self, *model_parameters):
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_aic_grouped_cumulative(cumulative_failures, *model_parameters)

    def calculate_aic_grouped_fpd(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)
