from abc import abstractmethod
from functools import partial

import numpy as np
import scipy.optimize as opt
from colorama import Fore, Back
from scipy import integrate

from src.auxiliar_math import gamma
from src.domain.models.pure_births_estimator import PureBirthsEstimator


class NHPPEstimator(PureBirthsEstimator):

    def __init__(self, saddlepoint_calculator):
        self.saddlepoint_calculator = saddlepoint_calculator

    @abstractmethod
    def calculate_mean(self, t, *model_parameters):
        pass

    @abstractmethod
    def calculate_lambda(self, t, *model_parameters):
        pass

    @abstractmethod
    def calculate_limit_for_mu(self, *model_parameters):
        pass

    def calculate_mean_failure_numbers(self, times, *model_parameters):
        return self.calculate_mean(np.array(times), *model_parameters)

    def fit_mean_failure_number_by_least_squares(self, times, cumulative_failures, initial_approx):
        parameters, cov = opt.curve_fit(self.calculate_mean, times, cumulative_failures, p0=initial_approx)
        return parameters

    # The methods 'hybr', 'lm' y 'krylov' are the only ones working for this particular problem.
    # For more details, read the docs:
    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.root.html
    def estimate_ttf_parameters_by_maximum_likelihood(self, times, initial_approx,
                                                      solving_method):
        try:
            return opt.root(partial(self.ttf_ml_equations, times), initial_approx,
                            method=solving_method).x
        except ValueError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            # TODO: Find a way to handle this exception
            # raise InvalidFitException(str(error))

    @abstractmethod
    def ttf_ml_equations(self, times, vec):
        pass

    def estimate_grouped_cumulative_parameters_by_maximum_likelihood(self, days, cumulative_failures,
                                                                     initial_approx, solving_method):
        try:
            return opt.root(partial(self.grouped_cumulative_ml_equations, days, cumulative_failures),
                            initial_approx, method=solving_method).x
        except ValueError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))

    @abstractmethod
    def grouped_cumulative_ml_equations(self, days, cumulative_failures, vec):
        pass

    def estimate_grouped_fpd_parameters_by_maximum_likelihood(self, times, failures_per_day, initial_approx,
                                                              solving_method):
        try:
            return opt.root(partial(self.grouped_fpd_ml_equations, times, failures_per_day), initial_approx,
                            method=solving_method).x
        except ValueError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))

    @abstractmethod
    def grouped_fpd_ml_equations(self, times, failures_per_day, vec):
        pass

    def calculate_prr(self, times, cumulative_failures, *model_parameters):
        # The first value is always zero. It has to be eliminated in order to allow the division
        times = times[1:]
        cumulative_failures = cumulative_failures[1:]

        estimated_failures = [self.calculate_mean(times[i], *model_parameters) for i in range(len(times))]
        prr = 0
        for i in range(len(times)):
            prr += (1 - cumulative_failures[i] / estimated_failures[i]) ** 2
        return prr

    def calculate_ttf_aic(self, times, *model_parameters):
        return -2 * self.ttf_log_likelihood(times, *model_parameters) + (2 * len(model_parameters))

    def calculate_aic_grouped_cumulative(self, cumulative_failures, *model_parameters):
        return -2 * self.grouped_cumulative_log_likelihood(cumulative_failures, *model_parameters) + (2 * len(model_parameters))

    def calculate_aic_grouped_fpd(self, failures_per_day, *model_parameters):
        return -2 * self.grouped_fpd_log_likelihood(failures_per_day, *model_parameters) + (2 * len(model_parameters))

    def ttf_log_likelihood(self, times, *model_parameters):
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, *model_parameters)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, *model_parameters)
        sum = 0
        for k in range(len(times)):
            t_k = times[k]
            lambda_tk = self.calculate_lambda(t_k, *model_parameters)
            sum += np.log(lambda_tk)
        return sum - (mu_tn - mu_t0)

    # At this moment, this code is not being used
    # The grouped cumulative data AIC is calculated using the FPD log likelihood (kinda hard-coded)
    def grouped_cumulative_log_likelihood(self, cumulative_failures, *model_parameters):
        times = np.arange(1, len(cumulative_failures) + 1)
        sum = 0
        n = len(times)
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, *model_parameters)
        for i in range(len(times)):
            t_i = times[i]
            y_i = cumulative_failures[i]
            mu_ti = self.calculate_mean(t_i, *model_parameters)
            y_i_factorial = np.math.factorial(y_i)
            sum += y_i * np.log(mu_ti - mu_t0) - np.math.log(y_i_factorial) - mu_ti
        return sum + n * mu_t0

    def grouped_fpd_log_likelihood(self, failures_per_day, *model_parameters):
        times = np.arange(1, len(failures_per_day) + 1)
        sum = 0
        deltas_yi = failures_per_day
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, *model_parameters)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, *model_parameters)
        for i in range(len(times)):
            t_i = times[i]
            delta_y_i = deltas_yi[i]
            mu_ti = self.calculate_mean(t_i, *model_parameters)
            if i == 0:
                t_i_minus_1 = t_0
            else:
                t_i_minus_1 = times[i - 1]
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, *model_parameters)
            delta_y_i_factorial = np.math.factorial(delta_y_i)
            sum += (delta_y_i * np.log(mu_ti - mu_ti_minus_1)) - np.math.log(delta_y_i_factorial)
        return sum - (mu_tn - mu_t0)

    def calculate_mttfs(self, n_failures, *model_parameters):
        upper_limit = self.calculate_limit_for_mu(*model_parameters)
        mttfs = []
        wasnan = False
        for k in range(1, n_failures + 1):
            if k==99:
                a=2
            if not wasnan:
                mttf = self.calculate_mttf(k, upper_limit, *model_parameters)
                if np.isnan(mttf):
                    wasnan = True
                    mttf = self.saddlepoint_calculator.calculate_saddlepoint_mttf_approximation(
                        k, upper_limit, *model_parameters)
            else:
                mttf = self.saddlepoint_calculator.calculate_saddlepoint_mttf_approximation(
                    k, upper_limit, *model_parameters)
            mttfs.append(mttf)
        return mttfs

    def calculate_mttf(self, k, upper_limit, *model_parameters):
        mttf = self.calculate_exact_mttf_integral(k, upper_limit, *model_parameters)
        return mttf

    def calculate_exact_mttf_integral(self, k, upper_limit, *model_parameters):
        denominator = gamma.lower_incomplete_gamma(upper_limit, k)
        numerator = integrate.quad(lambda u:
                                   (u * self.calculate_lambda(u, *model_parameters) *
                                    (self.calculate_mean(u, *model_parameters) ** (k - 1)) *
                                    np.exp(- self.calculate_mean(u, *model_parameters))),
                                   0, +np.inf, limit=2000)[0]
        return numerator / denominator

