import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestInitialSample(unittest.TestCase):

    ntds_go_fit_from_sample_10 = None

    @classmethod
    def setUpClass(cls):
        cls.ntds_go_fit_from_sample_10 = ModelFitter().fit('goel-okumoto', 'ntds', initial_sample=10,
                                                           mts=False, initial_approx=(50, 0.005))

    def test_ntds_goel_okumoto_with_a_partial_dataset_from_sample_10(self):
        a = TestInitialSample.ntds_go_fit_from_sample_10.get_ml_parameters()[0]
        b = TestInitialSample.ntds_go_fit_from_sample_10.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 36.575219, places=6)
        self.assertAlmostEqual(b, 0.009860, places=6)
