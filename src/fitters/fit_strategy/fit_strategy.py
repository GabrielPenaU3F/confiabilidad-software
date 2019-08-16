from abc import abstractmethod, ABC

from data.data_repository import DataRepository
from src.exceptions.exceptions import NotAdmittedFormatException


class FitStrategy(ABC):

    def __init__(self, project_name, model):
        self.project_name = project_name
        self.model = model
        self.data = DataRepository.provide_observed_data_from_project(project_name)

    @abstractmethod
    def fit_ttf(self):
        pass

    @abstractmethod
    def fit_grouped_cumulative(self):
        pass

    @abstractmethod
    def fit_grouped_fpd(self):
        pass

    @abstractmethod
    def calculate_prr(self):
        pass

    @abstractmethod
    def calculate_aic(self):
        pass

    def validate_format(self, data):
        if not data.get_format() == 'ttf':
            raise NotAdmittedFormatException('The chosen project does not admit the specified format')
