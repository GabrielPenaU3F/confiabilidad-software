from abc import ABC, abstractmethod

from src.exceptions.exceptions import InvalidArgumentException


class FormatStrategy(ABC):

    execute_ml_function = None

    def __init__(self, data, model):
        self.data = data
        self.model = model

    def determine_end_sample(self, end_sample_arg):
        if end_sample_arg is None:
            end = len(self.data.get_times())
        else:
            try:
                if end_sample_arg == int(end_sample_arg):
                    end = int(end_sample_arg)
            except TypeError:
                raise InvalidArgumentException('The end sample argument must be an integer')
        return end

    @abstractmethod
    def fit_model(self, **kwargs):
        pass

    def determine_ml_parameters(self, lsq_only_arg, *ml_function_parameters):
        if lsq_only_arg is True:
            ml_params = None
        else:
            ml_params = self.execute_ml_function(*ml_function_parameters, solving_method='krylov')
        return ml_params

    @abstractmethod
    def determine_initial_approx(self, initial_approx_arg):
        pass

    @abstractmethod
    def calculate_aic(self, *model_parameters, **kwargs):
        pass
