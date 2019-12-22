import unittest

from src.domain.fitters.fitter import Fitter


class LogisticTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('logistic', 'mixed-waterfall-agile', initial_approx=(0.01, 0.001, 0.00001),
                               lsq_only=True)

    def test_mixed_waterfall_agile_logistic_least_squares_a_parameter_is_835_comma_410586(self):
        a = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 835.410586, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_b_parameter_is_0_comma_030741(self):
        b = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.030741, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_c_parameter_is_0_comma_801125(self):
        c = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 75.801125, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_prr_is_7_comma_001083(self):
        prr = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 7.001083, places=6)
