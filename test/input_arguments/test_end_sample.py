import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestEndSample(unittest.TestCase):

    fit_ds_agile1_25samples = None
    fit_log_agile1_25samples = None
    fit_ds_mixed_35samples = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ds_agile1_25samples = ModelFitter().fit('delayed-s-shaped', 'agile-n1', end_sample=25, mts=False)
        cls.fit_log_agile1_25samples = ModelFitter().fit('logistic', 'agile-n1', end_sample=25, mts=False)
        cls.fit_ds_mixed_35samples = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=35, mts=False)

    def test_agile_n1_delayed_s_shaped_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 70.048405, places=6)
        self.assertAlmostEqual(b, 0.003215, places=6)

    def test_agile_n1_logistic_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 28.432855, places=6)
        self.assertAlmostEqual(b, 0.013269, places=6)
        self.assertAlmostEqual(c, 256.198828, places=6)

    def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_35_samples(self):
        a = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 141.063266, places=6)
        self.assertAlmostEqual(b, 0.131726, places=6)
