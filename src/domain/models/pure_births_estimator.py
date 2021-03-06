from abc import ABC, abstractmethod

import numpy as np
from scipy import integrate

from src.auxiliar_math.gamma import gamma


class PureBirthsEstimator(ABC):

    default_initial_approximations = None
    saddlepoint_calculator = None

    def __init__(self, saddlepoint_calculator):
        self.saddlepoint_calculator = saddlepoint_calculator

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

    def calculate_regular_mttfs(self, data, *model_parameters):
        n_failures = data.get_cumulative_failures()[-1]
        upper_limit = self.calculate_limit_for_mu(*model_parameters)
        mttfs = []
        wasnan = False
        for k in range(1, n_failures + 1):
            if not wasnan:
                mttf = self.calculate_exact_mttf_integral(k, upper_limit, *model_parameters)
                if np.isnan(mttf):
                    wasnan = True
                    mttf = self.saddlepoint_calculator.calculate_saddlepoint_mttf_approximation(
                        k, upper_limit, *model_parameters)
            else:
                mttf = self.saddlepoint_calculator.calculate_saddlepoint_mttf_approximation(
                    k, upper_limit, *model_parameters)
            mttfs.append(mttf)
        return mttfs

    def calculate_conditional_mttfs(self, data, *model_parameters):
        mtbfs = self.calculate_conditional_mtbfs(data, *model_parameters)
        mttfs = np.cumsum(mtbfs)
        return mttfs

    def calculate_regular_mtbfs(self, mttfs):
        mtbfs = [mttfs[0]]
        for k in range(1, len(mttfs)):
            mtbfs.append(mttfs[k] - mttfs[k - 1])
        return mtbfs

    def calculate_conditional_mtbfs(self, data, *model_parameters):
        mtbfs = []
        failure_times = data.get_times()
        n_failures = data.get_cumulative_failures()
        for i in range(len(n_failures)):
            # This returns the mtbf between failures i and i+1
            mtbfs.append(self.calculate_conditional_mtbf(n_failures[i], failure_times[i], *model_parameters))
        return mtbfs

    def calculate_conditional_mtbf(self, n, t_n, *model_parameters):
        pass

    @abstractmethod
    def calculate_prr(self, *parameters):
        pass

    def get_default_initial_approx(self, format):
        return self.default_initial_approximations.get(format)

    def calculate_exact_mttf_integral(self, k, upper_limit, *model_parameters):
        denominator = gamma.lower_incomplete_gamma(upper_limit, k)
        numerator = integrate.quad(lambda u:
                                   (u * self.calculate_lambda(k, u, *model_parameters) *
                                   (self.calculate_mean(u, *model_parameters) ** (k - 1)) *
                                   np.exp(- self.calculate_mean(u, *model_parameters))),
                                   0, +np.inf, limit=2000)[0]
        try:
            mttf = numerator / denominator
        except OverflowError:
            mttf = np.nan
        return mttf
