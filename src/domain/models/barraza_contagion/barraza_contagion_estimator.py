import numpy as np
import scipy.optimize as opt

from src.domain.models.pure_births_estimator import PureBirthsEstimator
from src.domain.saddlepoint_calculators.barraza_contagion_saddlepoint_calculator import \
    BarrazaContagionSaddlepointCalculator


class BarrazaContagionEstimator(PureBirthsEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': (1, 0.5),
            'grouped-fpd': (1, 0.5)
        }
        self.bounds = ([0, 0], [+np.inf, +np.inf])
        saddlepoint_calculator = BarrazaContagionSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        a, b = model_parameters
        parenthesis = 1 + np.multiply(a, t)
        sq_brackets = np.power(parenthesis, b) - 1
        return sq_brackets/b

    def calculate_lambda(self, r, t, *model_parameters):
        a, b = model_parameters
        numerator = 1 + b * r
        denominator = 1 + a * t
        return a * numerator / denominator

    def calculate_limit_for_mu(self, *model_parameters):
        return +np.inf

    def calculate_mean_failure_numbers(self, times, *model_parameters):
        return self.calculate_mean(np.array(times), *model_parameters)

    def fit_mean_failure_number_by_least_squares(self, times, cumulative_failures, initial_approx):
        parameters, cov = opt.curve_fit(self.calculate_mean, times, cumulative_failures, p0=initial_approx,
                                        bounds=self.bounds)
        return parameters

    def estimate_ttf_parameters_by_maximum_likelihood(self, *parameters, **kwargs):
        pass

    def estimate_grouped_fpd_parameters_by_maximum_likelihood(self, *parameters, **kwargs):
        pass

    def ttf_ml_equations(self):
        return None

    def grouped_fpd_ml_equations(self):
        return None

    def calculate_mttfs(self, mt_formula, data, *model_parameters):
        if mt_formula == 'conditional':
            failure_times = data.get_times()
            mttfs = []
            mttfs.append(self.calculate_conditional_mtbf(failure_times[0], *model_parameters))
            for k in range(1, len(failure_times)):
                mttfs.append(mttfs[k-1] + self.calculate_conditional_mtbf(failure_times[k], *model_parameters))
            return mttfs
        elif mt_formula == 'regular':
            n_failures = data.get_cumulative_failures()[-1]
            return super().calculate_mttfs(n_failures, *model_parameters)

    def calculate_mtbfs(self, mttfs):
        return super().calculate_mtbfs(mttfs)

    def calculate_conditional_mtbf(self, n_failure_time, *model_parameters):
        a, b = model_parameters
        parenthesis = 1 + a * n_failure_time
        return parenthesis / (a * (parenthesis**b - 1))

    def calculate_prr(self, times, cumulative_failures, *model_parameters):
        estimated_failures = [self.calculate_mean(times[i], *model_parameters) for i in range(len(times))]
        prr = 0
        for i in range(len(times)):
            prr += (1 - cumulative_failures[i] / estimated_failures[i]) ** 2
        return prr
