from src.fitters.format_strategy.format_strategy import FormatStrategy


class FPDFormatStrategy(FormatStrategy):

    def calculate_aic(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)

    # Since I haven't found a straightforward way to put this inside the design, because the
    # 'cumulative' is not an actual format, this code is not being used at all.
    # The same applies to the log likelihood function.
    # Todo: eliminate the grouped cumulative equations, or find a way to reach this code
    def calculate_aic_grouped_cumulative(self, *model_parameters):
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_aic_grouped_cumulative(cumulative_failures, *model_parameters)
