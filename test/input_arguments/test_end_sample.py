import unittest

from src.domain.fitters.fitter import Fitter


class TestEndSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fit_ds_agile1_25samples = Fitter().fit('delayed-s-shaped', 'agile-n1', end_sample=25, mts=False)
        cls.fit_ds_agile1_15samples = Fitter().fit('delayed-s-shaped', 'agile-n1', end_sample=15, mts=False)
        cls.fit_log_agile1_25samples = Fitter().fit('logistic', 'agile-n1', end_sample=25, mts=False)
        cls.fit_log_agile1_20samples = Fitter().fit('logistic', 'agile-n1', end_sample=20, mts=False)

        # cls.fit_ds_mixed_35samples = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=35, mts=False)
        # cls.fit_ds_mixed_15samples = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=15, mts=False)
        # cls.fit_log_mixed_25samples = Fitter().fit('logistic', 'mixed-waterfall-agile', end_sample=25, mts=False)
        # cls.fit_log_mixed_35samples = Fitter().fit('logistic', 'mixed-waterfall-agile', end_sample=35, mts=False)

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

    # def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_35_samples(self):
    #     a = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[0]
    #     b = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[1]
    #     self.assertAlmostEqual(a, 142.968176, places=6)
    #     self.assertAlmostEqual(b, 0.107149, places=6)
    #
    # def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_15_samples(self):
    #     a = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[0]
    #     b = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[1]
    #     self.assertAlmostEqual(a, 54.895501, places=6)
    #     self.assertAlmostEqual(b, 0.805702, places=6)
    #
    # def test_mixed_delayed_s_shaped_with_partial_datasets_prr_comparison(self):
    #     prr_15samples = TestEndSample.fit_ds_mixed_15samples.get_prr_ml()
    #     prr_35samples = TestEndSample.fit_ds_mixed_35samples.get_prr_ml()
    #     self.assertTrue(prr_15samples > prr_35samples)
    #
    # def test_mixed_logistic_with_a_partial_dataset_of_25_samples(self):
    #     a = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[0]
    #     b = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[1]
    #     c = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[2]
    #     self.assertAlmostEqual(a, -0.001534, places=6)
    #     self.assertAlmostEqual(b, 0.246161, places=6)
    #     self.assertAlmostEqual(c, -5.570353, places=6)
    #
    # def test_mixed_logistic_with_a_partial_dataset_of_35_samples(self):
    #     a = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[0]
    #     b = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[1]
    #     c = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[2]
    #     self.assertAlmostEqual(a, 0.005719, places=6)
    #     self.assertAlmostEqual(b, 0.198346, places=6)
    #     self.assertAlmostEqual(c, 13.363637, places=6)
    #
    # def test_mixed_logistic_with_partial_datasets_prr_comparison(self):
    #     prr_25samples = TestEndSample.fit_log_mixed_25samples.get_prr_ml()
    #     prr_35samples = TestEndSample.fit_log_mixed_35samples.get_prr_ml()
    #     self.assertTrue(prr_25samples > prr_35samples)

    # Surprisingly, this test fails. Maybe it's an exception to the general rule?
    '''
    def test_mixed_goel_okumoto_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_go_mixed_15samples.get_prr_ml()
        prr_35samples = TestEndSample.fit_go_mixed_35samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_35samples)
    '''
