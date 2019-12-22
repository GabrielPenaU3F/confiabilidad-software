from src.domain.fitters.format_strategy.format_strategy import FormatStrategy


class GroupedFPDFormatStrategy(FormatStrategy):

    def __init__(self, data, model):
        super().__init__(data, model)
        self.execute_ml_function = self.model.estimate_grouped_fpd_parameters_by_maximum_likelihood

    def fit_model(self, optional_arguments):

        optional_arguments = self.set_initial_approx(optional_arguments)

        end = self.determine_end_sample(optional_arguments.get_end_sample())

        fpd = self.data.get_data()[0:end]
        cumulative_failures = self.data.get_cumulative_failures()[0:end]

        y0 = optional_arguments.get_x0()
        fpd.insert(0, y0)
        cumulative_failures.insert(0, y0)
        times = self.data.get_times()[0:end]
        times.insert(0, 0)

        lsq_params = self.model.fit_mean_failure_number_by_least_squares(times, cumulative_failures,
                                                                         optional_arguments)
        optional_arguments.set_initial_approx(lsq_params)
        ml_function_parameters = optional_arguments.get_lsq_only(), times, fpd, optional_arguments
        ml_params = self.determine_ml_estimates(*ml_function_parameters)
        return lsq_params, ml_params

    def set_initial_approx(self, optional_arguments):
        return self.determine_initial_approx(optional_arguments, 'grouped-fpd')

    def calculate_aic(self, *model_parameters):
        fpd = self.data.get_data()
        return self.model.calculate_aic_grouped_fpd(fpd, *model_parameters)
