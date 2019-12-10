import unittest

from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from src.domain.saddlepoint_calculators.delayed_s_shaped_saddlepoint_calculator import \
    DelayedSShapedSaddlepointCalculator


class DSSaddlepointCalculatorTest(unittest.TestCase):

    a = 893.6389
    b = 0.0218

    def test_ds_mttf_saddlepoint_approx_for_k_150_mixed_dataset(self):
        k = 150
        ds = DelayedSShapedEstimator()
        calculator = DelayedSShapedSaddlepointCalculator(ds.calculate_lambda, ds.calculate_mean)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b)
        self.assertAlmostEqual(33, saddlepoint_approx, delta=1)
