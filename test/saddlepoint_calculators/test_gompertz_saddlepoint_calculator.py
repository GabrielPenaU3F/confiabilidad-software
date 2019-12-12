import unittest

import numpy as np

from src.domain.models.gompertz.gompertz_estimator import GompertzEstimator
from src.domain.saddlepoint_calculators.gompertz_saddlepoint_calculator import GompertzSaddlepointCalculator


class GompertzSaddlepointCalculatorTest(unittest.TestCase):

    a = 1093.6277
    b = 0.0940
    c = 0.9850

    def test_gompertz_mttf_saddlepoint_approx_for_k_100_mixed_dataset_is_0_comma_7(self):
        k = 100
        gompertz = GompertzEstimator()
        calculator = GompertzSaddlepointCalculator(gompertz.calculate_mean, gompertz.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b, self.c)
        self.assertAlmostEqual(0.7, saddlepoint_approx, delta=1)

    def test_gompertz_mttf_saddlepoint_approx_for_k_600_mixed_dataset_is_90(self):
        k = 600
        gompertz = GompertzEstimator()
        calculator = GompertzSaddlepointCalculator(gompertz.calculate_mean, gompertz.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b, self.c)
        self.assertAlmostEqual(90, saddlepoint_approx, delta=1)

    def test_gompertz_mttf_saddlepoint_approx_for_k_900_mixed_dataset_is_161(self):
        k = 900
        gompertz = GompertzEstimator()
        calculator = GompertzSaddlepointCalculator(gompertz.calculate_mean, gompertz.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b, self.c)
        self.assertAlmostEqual(161, saddlepoint_approx, delta=1)
