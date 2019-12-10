import unittest

from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator
from src.domain.saddlepoint_calculators.goel_okumoto_saddlepoint_calculator import GoelOkumotoSaddlepointCalculator
from src.fitters.fitter import GroupedFPDFitter


class GOSaddlepointCalculatorTest(unittest.TestCase):

    a = 1373.2903
    b = 0.0050

    def test_go_mttf_saddlepoint_approx_for_k_100_mixed_dataset_is_15(self):
        k = 100
        go = GoelOkumotoEstimator()
        calculator = GoelOkumotoSaddlepointCalculator(go.calculate_mean, go.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b)
        self.assertAlmostEqual(15, saddlepoint_approx, delta=1)

    def test_go_mttf_saddlepoint_approx_for_k_600_mixed_dataset_is_114(self):
        k = 600
        go = GoelOkumotoEstimator()
        calculator = GoelOkumotoSaddlepointCalculator(go.calculate_mean, go.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b)
        self.assertAlmostEqual(114, saddlepoint_approx, delta=1)

    def test_go_mttf_saddlepoint_approx_for_k_900_mixed_dataset_is_212(self):
        k = 900
        go = GoelOkumotoEstimator()
        calculator = GoelOkumotoSaddlepointCalculator(go.calculate_mean, go.calculate_lambda)
        saddlepoint_approx = calculator.calculate_saddlepoint_mttf_approximation(k, self.a, self.a, self.b)
        self.assertAlmostEqual(212, saddlepoint_approx, delta=1)
