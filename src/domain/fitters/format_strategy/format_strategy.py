from abc import ABC, abstractmethod

from src.exceptions.exceptions import InvalidArgumentException


class FormatStrategy(ABC):

    execute_ml_function = None

    def __init__(self, data, model):
        self.data = data
        self.model = model

    def determine_end_sample(self, end_sample_arg):
        default_end_sample = len(self.data.get_times())
        if end_sample_arg > default_end_sample:
            raise InvalidArgumentException('The end sample must not exceed the length of the dataset')
        if end_sample_arg != 0:
            return end_sample_arg
        else:
            return default_end_sample

    @abstractmethod
    def fit_model(self, optional_arguments):
        pass

    def determine_ml_estimates(self, lsq_only_arg, *ml_function_parameters):
        if lsq_only_arg is True:
            ml_estimates = None
        else:
            ml_estimates = self.execute_ml_function(*ml_function_parameters, solving_method='krylov')
        return ml_estimates

    def determine_initial_approx(self, optional_arguments, format):
        initial_approx_arg = optional_arguments.get_initial_approx()
        if initial_approx_arg is not None:
            return optional_arguments
        else:
            optional_arguments.set_initial_approx(self.model.get_default_initial_approx(str(format)))
            return optional_arguments

    @abstractmethod
    def set_initial_approx(self, optional_arguments):
        pass

    @abstractmethod
    def calculate_aic(self, *model_parameters, **kwargs):
        pass