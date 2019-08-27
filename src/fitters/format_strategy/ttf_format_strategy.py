from src.exceptions.exceptions import InvalidArgumentException
from src.fitters.format_strategy.format_strategy import FormatStrategy


class TTFFormatStrategy(FormatStrategy):

    def calculate_aic(self, *model_parameters, **kwargs):
        if len(kwargs) > 0:
            raise InvalidArgumentException("The TTF format does not allow any optional arguments")
        original_times = self.data.get_data()
        return self.model.calculate_ttf_aic(original_times, *model_parameters)
