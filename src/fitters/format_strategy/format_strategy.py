from abc import ABC, abstractmethod


class FormatStrategy(ABC):

    def __init__(self, data, model):
        self.data = data
        self.model = model

    @abstractmethod
    def fit_model(self, **kwargs):
        pass

    @abstractmethod
    def determine_initial_approx(self, initial_approx_arg):
        pass

    @abstractmethod
    def calculate_aic(self, *model_parameters, **kwargs):
        pass
