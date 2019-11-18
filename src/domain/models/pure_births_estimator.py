from abc import ABC, abstractmethod


class PureBirthsEstimator(ABC):

    @abstractmethod
    def calculate_mean(self, *parameters):
        pass

    @abstractmethod
    def calculate_lambda(self, *parameters):
        pass

    @abstractmethod
    def calculate_limit_for_mu(self, *model_parameters):
        pass

    @abstractmethod
    def fit_mean_failure_number_by_least_squares(self, *parameters):
        pass

    @abstractmethod
    def estimate_ttf_parameters_by_maximum_likelihood(self, *parameters):
        pass

    @abstractmethod
    def estimate_grouped_fpd_parameters_by_maximum_likelihood(self, *parameters):
        pass

    @abstractmethod
    def calculate_mttfs(self, *parameters):
        pass

    @abstractmethod
    def calculate_mtbfs(self, *parameters):
        pass

    @abstractmethod
    def calculate_prr(self, *parameters):
        pass
