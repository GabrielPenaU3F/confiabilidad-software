from abc import ABC, abstractmethod

import numpy as np


class PureBirthsEstimator(ABC):

    default_initial_approximations = None

    @abstractmethod
    def calculate_mean(self, *parameters):
        pass

    @abstractmethod
    def calculate_lambda(self, *parameters):
        pass

    @abstractmethod
    def calculate_limit_for_mu(self, *model_parameters):
        pass

    def calculate_mean_failure_numbers(self, *parameters):
        times, failures_by_time, *model_parameters = parameters
        return self.calculate_mean(np.array(times), *model_parameters)

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

    def calculate_mtbfs(self, mttfs):
        mtbfs = [mttfs[0]]
        for k in range(1, len(mttfs)):
            mtbfs.append(mttfs[k] - mttfs[k - 1])
        return mtbfs

    @abstractmethod
    def calculate_prr(self, *parameters):
        pass

    def get_default_initial_approx(self, format):
        return self.default_initial_approximations.get(format)
