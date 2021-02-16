import unittest

from src.domain.fitters.model_fitter import ModelFitter


class HomogeneousPoissonTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('poisson', 'mixed-waterfall-agile', initial_approx=0.5, mts=False)

    def test_mixed_waterfall_agile_homogeneous_poisson_maximum_likelihood_a_parameter_is_4_comma_239234(self):
        a = self.__class__.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 4.239234, places=6)

    def test_mixed_waterfall_agile_homogeneous_poisson_maximum_likelihood_prr_is_32_comma_397142(self):
        prr = self.__class__.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 32.397142, places=6)

    def test_mixed_waterfall_agile_homogeneous_poisson_aic_is_1366_comma_889271(self):
        aic = self.__class__.fit.get_aic()
        self.assertAlmostEqual(aic, 1366.889271, places=6)
