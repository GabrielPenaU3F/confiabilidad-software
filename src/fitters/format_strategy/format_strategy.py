from abc import ABC, abstractmethod


class FormatStrategy(ABC):

    def __init__(self, data, model):
        self.data = data
        self.model = model

    @abstractmethod
    def calculate_aic(self, *model_parameters):
        pass
