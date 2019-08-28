import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class LogisticTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('logistic', 'mixed-waterfall-agile')

    # Method not working yet
    '''
    def test_mixed_waterfall_agile_goel_okumoto_least_squares_a_parameter_is_1416_comma_913890(self):
        a = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 1416.913890, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_b_parameter_is_0_comma_004806(self):
        b = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.004807, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_c_parameter_is_0_comma_004806(self):
        c = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.004807, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_prr_is_9_comma_015730(self):
        prr = LogisticTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 9.015730, places=6)
        
    '''