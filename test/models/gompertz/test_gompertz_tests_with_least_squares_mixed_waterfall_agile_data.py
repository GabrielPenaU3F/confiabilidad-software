import unittest

from src.domain.fitters.fitter import GroupedFPDFitter


class GompertzTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFPDFitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5))

    def test_mixed_waterfall_agile_gompertz_least_squares_a_parameter_is_885_comma_879217(self):
        a = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 885.879217, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_b_parameter_is_0_comma_040079(self):
        b = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.040079, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_c_parameter_is_0_comma_980457(self):
        c = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.980457, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_prr_is_2_comma_522043(self):
        prr = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2.522043, places=6)
