from abc import ABC, abstractmethod


class ModelEstimator(ABC):

    @abstractmethod
    def calculate_mean(self, t, *model_parameters):
        pass

    @abstractmethod
    def calculate_lambda(self, t, *model_parameters):
        pass

    @abstractmethod
    def calculate_limit_for_mu(self, *model_parameters):
        pass

    @abstractmethod
    def fit_mean_failure_number_by_least_squares(self, times, cumulative_failures, initial_approx):
        pass

    @abstractmethod
    def calculate_mttf(self, n_fallas, *model_parameters):
        pass

    @abstractmethod
    def calculate_mtbf(self, mttf):
        pass