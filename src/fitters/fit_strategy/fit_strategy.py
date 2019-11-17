from abc import ABC

from src.data.data_repository import DataRepository
from src.fitters.format_strategy.grouped_fpd_format_strategy import GroupedFPDFormatStrategy
from src.fitters.format_strategy.ttf_format_strategy import TTFFormatStrategy


class FitStrategy(ABC):

    def __init__(self, project_name, model):
        self.project_name = project_name
        self.model = model
        self.data = DataRepository.provide_project_data(project_name)
        self.format_strategies = {
            'ttf': TTFFormatStrategy,
            'grouped': GroupedFPDFormatStrategy
        }

    def get_project_name(self):
        return self.project_name

    def get_data(self):
        return self.data

    def get_model(self):
        return self.model

    def fit_model(self, format_strategy, **kwargs):
        return format_strategy.fit_model(**kwargs)

    def calculate_prr(self, *model_parameters):
        times = self.data.get_times()
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_prr(times, cumulative_failures, *model_parameters)

    def calculate_aic(self, *model_parameters):
        strategy = self.format_strategies.get(self.data.get_format())(self.data, self.model)
        return strategy.calculate_aic(*model_parameters)

    def calculate_mttfs(self, *model_parameters):
        return self.model.calculate_mttfs(self.data.get_cumulative_failures()[-1], *model_parameters)

    def calculate_mtbfs(self, mttfs):
        return self.model.calculate_mtbfs(mttfs)
