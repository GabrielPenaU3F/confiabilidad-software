from abc import abstractmethod, ABC

from src.data.data_repository import DataRepository
from src.fitters.format_strategy.fpd_format_strategy import FPDFormatStrategy
from src.fitters.format_strategy.ttf_format_strategy import TTFFormatStrategy


class FitStrategy(ABC):

    def __init__(self, project_name, model):
        self.project_name = project_name
        self.model = model
        self.data = DataRepository.provide_project_data(project_name)
        self.format_strategies = {
            'ttf': TTFFormatStrategy,
            'grouped': FPDFormatStrategy
        }

    def get_project_name(self):
        return self.project_name

    def get_model(self):
        return self.model

    @abstractmethod
    def fit_ttf(self):
        pass

    @abstractmethod
    def fit_grouped_cumulative(self):
        pass

    @abstractmethod
    def fit_grouped_fpd(self):
        pass

    def calculate_prr(self, *model_parameters):
        times = self.data.get_times()
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_prr(times, cumulative_failures, *model_parameters)

    def calculate_aic(self, *model_parameters):
        strategy = self.format_strategies.get(self.data.get_format())(self.data, self.model)
        return strategy.calculate_aic(*model_parameters)
