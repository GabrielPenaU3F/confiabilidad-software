import unittest

from src.domain.fitters.model_fitter import ModelFitter


class HomogeneousPoissonTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('poisson', 'ntds', initial_approx=0.5, lsq_only=True, mts=False)

    def test_ntds_homogeneous_poisson_least_squares_a_parameter_is_0_comma_129135(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 0.129135, places=6)

    def test_ntds_homogeneous_poisson_least_squares_prr_is_1_comma_708796(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.708796, places=6)
