from abc import ABC

from src.data.data_formater import DataFormater
from src.data.data_repository import DataRepository
from src.domain.fitters.format_strategy.fpd_format_strategy import FPDFormatStrategy
from src.domain.fitters.format_strategy.ttf_format_strategy import TTFFormatStrategy
from src.exceptions.exceptions import InvalidArgumentException


class FitStrategy(ABC):

    def __init__(self, project_name, model):
        self.project_name = project_name
        self.model = model
        self.data = DataRepository.provide_project_data(project_name)
        self.format_strategies = {
            'ttf': TTFFormatStrategy,
            'fpd': FPDFormatStrategy
        }
        self.format_strategy = self.choose_format_strategy(self.data.get_format())

    def get_project_name(self):
        return self.project_name

    def get_data(self):
        return self.data

    def get_model(self):
        return self.model

    def get_format_strategy(self):
        return self.format_strategy

    def fit_model(self, optional_arguments):
        return self.format_strategy.fit_model(optional_arguments)

    def calculate_prr(self, *model_parameters):
        times = self.data.get_times()
        cumulative_failures = self.data.get_cumulative_failures()
        return self.model.calculate_prr(times, cumulative_failures, *model_parameters)

    def calculate_stage_prr(self, optional_arguments, *model_parameters):
        start = optional_arguments.get_initial_sample()
        end = optional_arguments.get_end_sample()
        times, cumulative_failures = DataFormater.slice_data(start, end,
                                                             self.data.get_times(), self.data.get_cumulative_failures())
        return self.model.calculate_prr(times, cumulative_failures, *model_parameters)

    def calculate_aic(self, *model_parameters):
        strategy = self.format_strategies.get(self.data.get_format())(self.data, self.model)
        return strategy.calculate_aic(*model_parameters)

    def calculate_mttfs(self, optional_arguments, *model_parameters):
        return self.model.calculate_mttfs(self.data.get_cumulative_failures()[-1], *model_parameters)

    def calculate_mtbfs(self, optional_arguments, mttfs):
        return self.model.calculate_mtbfs(mttfs)

    def choose_format_strategy(self, format):
        if not self.format_strategies.keys().__contains__(format):
            raise InvalidArgumentException('The data format is invalid')
        return self.format_strategies.get(format)(self.data, self.model)
