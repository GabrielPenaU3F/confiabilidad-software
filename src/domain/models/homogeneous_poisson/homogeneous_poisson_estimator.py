import numpy as np

from src.domain.models.nhpp_estimator import NHPPEstimator
from src.domain.saddlepoint_calculators.homogeneous_poisson_saddlepoint_calculator import \
    HomogeneousPoissonSaddlepointCalculator


class HomogeneousPoissonEstimator(NHPPEstimator):

    def __init__(self):
        self.default_initial_approximations = {
            'ttf': 0.5,
            'grouped-fpd': 0.5
        }
        self.bounds = (0, +np.inf)
        saddlepoint_calculator = HomogeneousPoissonSaddlepointCalculator(self.calculate_mean, self.calculate_lambda)
        super().__init__(saddlepoint_calculator)

    def calculate_mean(self, t, *model_parameters):
        lambda_ = model_parameters[0]
        return lambda_ * t

    def calculate_lambda(self, t, *model_parameters):
        return model_parameters[0]

    def calculate_limit_for_mu(self, *model_parameters):
        return np.inf

    def estimate_ttf_parameters_by_maximum_likelihood(self, times, initial_approx,
                                                      solving_method):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        t_n = times[-1]
        return [n / t_n - t_0]

    def estimate_grouped_fpd_parameters_by_maximum_likelihood(self, times, failures_per_day, initial_approx,
                                                              solving_method):
        t_0, times = self.separate_time_data(times)
        n = len(times)
        t_n = times[-1]
        deltas_yi = failures_per_day
        sum_deltas_yi = np.sum(deltas_yi)
        return [sum_deltas_yi / (t_n - t_0)]

    def ttf_ml_equations(self, times, vec):
        pass

    def grouped_fpd_ml_equations(self, times, failures_per_day, vec):
        pass

    def calculate_prr(self, times, cumulative_failures, *model_parameters):
        lambda_ = model_parameters[0]
        # The first value is always zero. It has to be eliminated in order to allow the division
        times = times[1:]
        cumulative_failures = cumulative_failures[1:]
        estimated_failures = []
        for i in range(len(times)):
            estimated_failures.append(self.calculate_mean(times[i], lambda_))
        prr = 0
        for i in range(len(times)):
            prr += (1 - cumulative_failures[i] / estimated_failures[i]) ** 2
        return prr

    def calculate_mttfs(self, n_failures, *model_parameters):
        lambda_ = model_parameters[0]
        mttfs = []
        for k in range(1, n_failures + 1):
            mttf = k / lambda_
            mttfs.append(mttf)
        return mttfs
