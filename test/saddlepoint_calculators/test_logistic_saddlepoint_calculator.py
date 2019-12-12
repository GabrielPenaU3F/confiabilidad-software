import unittest

import numpy as np

from src.domain.models.logistic.logistic_estimator import LogisticEstimator
from src.domain.saddlepoint_calculators.logistic_saddlepoint_calculator import LogisticSaddlepointCalculator


class LogisticSaddlepointCalculatorTest(unittest.TestCase):

    a = 1093.6277
    b = 0.0940
    c = 0.9850

    def test_logistic_mttf_saddlepoint_approx_for_k_900_mixed_dataset_is_194(self):
        k = 900
        logistic = LogisticEstimator()
        calculator = LogisticSaddlepointCalculator(logistic.calculate_mean, logistic.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b, self.c)
        self.assertAlmostEqual(194, saddlepoint_approx, delta=1)
