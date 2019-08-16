from abc import abstractmethod, ABC

from src.exceptions.exceptions import NotAdmittedFormatException


class FitStrategy(ABC):

    @abstractmethod
    def fit_ttf(self, project_name):
        pass

    @abstractmethod
    def fit_grouped_cumulative(self, project_name):
        pass

    @abstractmethod
    def fit_grouped_fpd(self, project_name):
        pass

    @abstractmethod
    def calculate_prr(self, project_name):
        pass

    @abstractmethod
    def calculate_aic(self, project_name):
        pass

    def validate_format(self, data):
        if not data.get_format() == 'ttf':
            raise NotAdmittedFormatException('The chosen project does not admit the specified format')
