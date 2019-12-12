import unittest

import numpy as np

from src.domain.models.musa_okumoto.musa_okumoto_estimator import MusaOkumotoEstimator
from src.domain.saddlepoint_calculators.musa_okumoto_saddlepoint_calculator import MusaOkumotoSaddlepointCalculator


class MOSaddlepointCalculatorTest(unittest.TestCase):

    a = 988.8479
    b = 0.0069

    def test_mo_mttf_saddlepoint_approx_for_k_100_mixed_dataset_is_15(self):
        k = 100
        mo = MusaOkumotoEstimator()
        calculator = MusaOkumotoSaddlepointCalculator(mo.calculate_mean, mo.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, np.inf, self.a, self.b)
        self.assertAlmostEqual(15, saddlepoint_approx, delta=1)

    def test_mo_mttf_saddlepoint_approx_for_k_600_mixed_dataset_is_120(self):
        k = 600
        mo = MusaOkumotoEstimator()
        calculator = MusaOkumotoSaddlepointCalculator(mo.calculate_mean, mo.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, np.inf, self.a, self.b)
        self.assertAlmostEqual(120, saddlepoint_approx, delta=1)

    def test_mo_mttf_saddlepoint_approx_for_k_900_mixed_dataset_is_215(self):
        k = 900
        mo = MusaOkumotoEstimator()
        calculator = MusaOkumotoSaddlepointCalculator(mo.calculate_mean, mo.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, np.inf, self.a, self.b)
        self.assertAlmostEqual(215, saddlepoint_approx, delta=1)
