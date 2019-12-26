import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestEndSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fit_ds_agile1_25samples = ModelFitter().fit('delayed-s-shaped', 'agile-n1', end_sample=25, mts=False)
        cls.fit_ds_agile1_15samples = ModelFitter().fit('delayed-s-shaped', 'agile-n1', end_sample=15, mts=False)
        cls.fit_log_agile1_25samples = ModelFitter().fit('logistic', 'agile-n1', end_sample=25, mts=False)
        cls.fit_log_agile1_20samples = ModelFitter().fit('logistic', 'agile-n1', end_sample=20, mts=False)

        cls.fit_ds_mixed_35samples = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=35, mts=False)
        cls.fit_ds_mixed_15samples = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=15, mts=False)

    def test_agile_n1_delayed_s_shaped_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 81.034870, places=6)
        self.assertAlmostEqual(b, 0.002868, places=6)

    def test_agile_n1_delayed_s_shaped_with_a_partial_dataset_of_15_samples(self):
        a = TestEndSample.fit_ds_agile1_15samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_agile1_15samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 1287.189809, places=6)
        self.assertAlmostEqual(b, 0.000680, places=6)

    def test_agile_n1_delayed_s_shaped_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_ds_agile1_15samples.get_prr_ml()
        prr_25samples = TestEndSample.fit_ds_agile1_25samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_25samples)

    def test_agile_n1_logistic_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 27.046223, places=6)
        self.assertAlmostEqual(b, 0.013968, places=6)
        self.assertAlmostEqual(c, 247.624295, places=6)

    def test_agile_n1_logistic_with_a_partial_dataset_of_20_samples(self):
        a = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 22.300405, places=6)
        self.assertAlmostEqual(b, 0.016871, places=6)
        self.assertAlmostEqual(c, 219.020155, places=6)

    def test_agile_n1_logistic_with_partial_datasets_prr_comparison(self):
        prr_20samples = TestEndSample.fit_log_agile1_20samples.get_prr_ml()
        prr_25samples = TestEndSample.fit_log_agile1_25samples.get_prr_ml()
        self.assertTrue(prr_20samples > prr_25samples)

    def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_35_samples(self):
        a = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 132.455439, places=6)
        self.assertAlmostEqual(b, 0.142219, places=6)

    def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_15_samples(self):
        a = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 76.643482, places=6)
        self.assertAlmostEqual(b, 2.892067, places=6)

    def test_mixed_delayed_s_shaped_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_ds_mixed_15samples.get_prr_ml()
        prr_35samples = TestEndSample.fit_ds_mixed_35samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_35samples)
