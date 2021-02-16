import unittest

from src.domain.fitters.model_fitter import ModelFitter


class HomogeneousPoissonTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('poisson', 'mixed-waterfall-agile',
                                    initial_approx=0.5, lsq_only=True, mts=False)

    def test_mixed_waterfall_agile_homogeneous_poisson_least_squares_a_parameter_is_4_comma_805753(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 4.805753, places=6)

    def test_mixed_waterfall_agile_homogeneous_poisson_least_squares_prr_is_18_comma_304389(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 18.304389, places=6)
