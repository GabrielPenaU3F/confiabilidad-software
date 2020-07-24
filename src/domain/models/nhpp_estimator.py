from abc import abstractmethod
from functools import partial

import numpy as np
import scipy.optimize as opt
from colorama import Fore, Back
from scipy import integrate

from src.auxiliar_math.gamma import gamma
from src.domain.models.pure_births_estimator import PureBirthsEstimator
from src.exceptions.exceptions import InvalidFitException


class NHPPEstimator(PureBirthsEstimator):

    bounds = None

    def __init__(self, saddlepoint_calculator):
        super().__init__(saddlepoint_calculator)

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
        parameters, cov = opt.curve_fit(self.calculate_mean, times, cumulative_failures, p0=initial_approx,
                                        bounds=self.bounds)
        return parameters

    # The methods 'hybr', 'lm' y 'krylov' are the only ones working for this particular problem.
    # For more details, read the docs:
    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.root.html
    def estimate_ttf_parameters_by_maximum_likelihood(self, times, initial_approx, solving_method):
        try:
            solution = opt.root(partial(self.ttf_ml_equations, times), initial_approx, method=solving_method).x
        except ValueError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            raise InvalidFitException(str(error))
        self.check_parameter_bounds(solution)
        return solution

    @abstractmethod
    def ttf_ml_equations(self, times, vec):
        pass

    def estimate_grouped_fpd_parameters_by_maximum_likelihood(self, times, failures_per_day, initial_approx,
                                                              solving_method):
        try:
            return opt.root(partial(self.grouped_fpd_ml_equations, times, failures_per_day), initial_approx,
                            method=solving_method).x
        except ValueError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            raise InvalidFitException(str(error))

    @abstractmethod
    def grouped_fpd_ml_equations(self, times, failures_per_day, vec):
        pass

    def calculate_prr(self, times, cumulative_failures, *model_parameters):
        estimated_failures = self.calculate_mean(np.array(times), *model_parameters)
        prr = 0
        for i in range(len(estimated_failures)):
            prr += (1 - cumulative_failures[i] / estimated_failures[i]) ** 2
        return prr

    def calculate_ttf_aic(self, times, *model_parameters):
        return -2 * self.ttf_log_likelihood(times, *model_parameters) + (2 * len(model_parameters))

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

    def separate_time_data(self, times):
        t_0 = times[0]
        times = times[1:len(times)]
        return t_0, times

    def check_parameter_bounds(self, ml_parameters):
        lower_bounds = self.bounds[0]
        upper_bounds = self.bounds[1]
        for i in range(len(ml_parameters)):
            parameter = ml_parameters[i]
            if parameter < lower_bounds[i] or parameter > upper_bounds[i]:
                raise InvalidFitException(
                    'ML equations returned an invalid solution. Try a different initial approximation')

    def calculate_exact_mttf_integral(self, k, upper_limit, *model_parameters):
        denominator = gamma.lower_incomplete_gamma(upper_limit, k)
        numerator = integrate.quad(lambda u:
                                   (u * self.calculate_lambda(u, *model_parameters) *
                                    (self.calculate_mean(u, *model_parameters) ** (k - 1)) *
                                    np.exp(- self.calculate_mean(u, *model_parameters))),
                                   0, +np.inf, limit=2000)[0]
        try:
            mttf = numerator / denominator
        except OverflowError:
            mttf = np.nan
        return mttf
