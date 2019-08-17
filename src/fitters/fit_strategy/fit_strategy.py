from abc import abstractmethod, ABC

from data.data_repository import DataRepository


class FitStrategy(ABC):

    def __init__(self, project_name, model):
        self.project_name = project_name
        self.model = model
        self.data = DataRepository.provide_project_data(project_name)

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

    def calculate_aic_ttf(self, *model_parameters):
        times = self.data.get_times()
        return self.model.calculate_ttf_aic(times, *model_parameters)

    def calculate_aic_grouped_cumulative(self):
        pass

    def calculate_aic_grouped_fpd(self):
        pass
