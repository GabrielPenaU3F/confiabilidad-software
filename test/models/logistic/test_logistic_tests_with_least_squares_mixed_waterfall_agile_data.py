import unittest

from src.domain.fitters.model_fitter import ModelFitter


class LogisticTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('logistic', 'mixed-waterfall-agile', initial_approx=(800, 0.03, 75),
                                    lsq_only=True, mts=False)

    def test_mixed_waterfall_agile_logistic_least_squares_a_parameter_is_835_comma_406794(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 835.406794, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_b_parameter_is_0_comma_030741(self):
        b = self.__class__.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.030741, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_c_parameter_is_0_comma_800545(self):
        c = self.__class__.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 75.800545, places=6)

    def test_mixed_waterfall_agile_logistic_least_squares_prr_is_7_comma_710604(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 7.710604, places=6)
