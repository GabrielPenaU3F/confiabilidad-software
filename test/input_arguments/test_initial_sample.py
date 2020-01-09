import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestInitialSample(unittest.TestCase):

    ntds_go_fit_from_sample_10 = None
    ntds_go_fit_from_sample_0 = None
    mixed_ds_fit_from_sample_40 = None
    mixed_ds_fit_from_sample_0 = None

    @classmethod
    def setUpClass(cls):
        cls.ntds_go_fit_from_sample_10 = ModelFitter().fit('goel-okumoto', 'ntds', initial_sample=10,
                                                           mts=False, initial_approx=(50, 0.005))
        cls.ntds_go_fit_from_sample_0 = ModelFitter().fit('goel-okumoto', 'ntds', initial_sample=0,
                                                          mts=False)
        cls.mixed_ds_fit_from_sample_40 = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile',
                                                            initial_sample=40, mts=False)
        cls.mixed_ds_fit_from_sample_0 = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile',
                                                           initial_sample=0, mts=False)

    def test_ntds_goel_okumoto_with_a_partial_dataset_from_sample_10(self):
        a = TestInitialSample.ntds_go_fit_from_sample_10.get_ml_parameters()[0]
        b = TestInitialSample.ntds_go_fit_from_sample_10.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 31.841272, places=6)
        self.assertAlmostEqual(b, 0.009446, places=6)

    def test_ntds_goel_okumoto_with_a_partial_dataset_from_sample_0_should_behave_as_if_not_specified(self):
        a = TestInitialSample.ntds_go_fit_from_sample_0.get_ml_parameters()[0]
        b = TestInitialSample.ntds_go_fit_from_sample_0.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 33.993503, places=6)
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_mixed_ds_with_a_partial_dataset_from_sample_40(self):
        a = TestInitialSample.mixed_ds_fit_from_sample_40.get_ml_parameters()[0]
        b = TestInitialSample.mixed_ds_fit_from_sample_40.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 981.474333, places=6)
        self.assertAlmostEqual(b, 0.022002, places=6)

    def test_mixed_ds_with_a_partial_dataset_from_sample_0_should_behave_as_if_not_specified(self):
        a = TestInitialSample.mixed_ds_fit_from_sample_0.get_ml_parameters()[0]
        b = TestInitialSample.mixed_ds_fit_from_sample_0.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 929.753752, places=6)
        self.assertAlmostEqual(b, 0.023049, places=6)

