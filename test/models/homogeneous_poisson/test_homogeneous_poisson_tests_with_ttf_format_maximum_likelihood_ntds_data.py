import unittest

from src.domain.fitters.model_fitter import ModelFitter


class HomogeneousPoissonTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('poisson', 'ntds', initial_approx=0.5)

    def test_ntds_homogeneous_poisson_maximum_likelihood_a_parameter_is_0_comma_104000(self):
        lambda_ = HomogeneousPoissonTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(lambda_, 0.104000, places=6)

    def test_ntds_homogeneous_poisson_maximum_likelihood_prr_is_5_comma_840390(self):
        prr = HomogeneousPoissonTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 5.840390, places=6)

    def test_ntds_homogeneous_poisson_aic_is_170_comma_694948(self):
        aic = HomogeneousPoissonTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 171.694948, places=6)
