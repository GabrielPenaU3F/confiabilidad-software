import unittest

from src.domain.fitters.fitter import GroupedFPDFitter


class LogisticTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFPDFitter().fit('logistic', 'mixed-waterfall-agile',
                                         initial_approx=(0.01, 0.001, 0.000001))

    def test_mixed_waterfall_agile_logistic_least_squares_a_parameter_is_835_comma_410609(self):
        a = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 835.410609, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_b_parameter_is_0_comma_030741(self):
        b = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.030741, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_c_parameter_is_0_comma_801129(self):
        c = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 75.801129, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_prr_is_7_comma_001084(self):
        prr = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 7.001084, places=6)
