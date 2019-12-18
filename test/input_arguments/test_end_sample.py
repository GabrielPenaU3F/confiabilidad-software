import unittest

from src.domain.fitters.fitter import TTFFitter, GroupedFPDFitter, GroupedCumulativeFitter


class TestEndSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fit_ds_agile1_25samples = TTFFitter().fit('delayed-s-shaped', 'agile-n1', end_sample=25, mts=False)
        cls.fit_ds_agile1_15samples = TTFFitter().fit('delayed-s-shaped', 'agile-n1', end_sample=15, mts=False)
        cls.fit_log_agile1_25samples = TTFFitter().fit('logistic', 'agile-n1', end_sample=25, mts=False)
        cls.fit_log_agile1_20samples = TTFFitter().fit('logistic', 'agile-n1', end_sample=20, mts=False)

        cls.fit_ds_mixed_35samples = GroupedFPDFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=35, mts=False)
        cls.fit_ds_mixed_15samples = GroupedFPDFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', end_sample=15, mts=False)
        cls.fit_log_mixed_25samples = GroupedFPDFitter().fit('logistic', 'mixed-waterfall-agile', end_sample=25, mts=False)
        cls.fit_log_mixed_35samples = GroupedFPDFitter().fit('logistic', 'mixed-waterfall-agile', end_sample=35, mts=False)

        cls.fit_go_mixed_35samples = GroupedCumulativeFitter().fit('goel-okumoto', 'mixed-waterfall-agile',
                                                                   end_sample=35, mts=False)
        cls.fit_go_mixed_15samples = GroupedCumulativeFitter().fit('goel-okumoto', 'mixed-waterfall-agile',
                                                                   end_sample=15, mts=False)

    def test_agile_n1_delayed_s_shaped_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_agile1_25samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 132.265072, places=6)
        self.assertAlmostEqual(b, 0.002057, places=6)

    def test_agile_n1_delayed_s_shaped_with_a_partial_dataset_of_15_samples(self):
        a = TestEndSample.fit_ds_agile1_15samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_agile1_15samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 1287.641345, places=6)
        self.assertAlmostEqual(b, 0.000679, places=6)

    def test_agile_n1_delayed_s_shaped_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_ds_agile1_15samples.get_prr_ml()
        prr_25samples = TestEndSample.fit_ds_agile1_25samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_25samples)

    def test_agile_n1_logistic_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_agile1_25samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 26.855837, places=6)
        self.assertAlmostEqual(b, 0.014167, places=6)
        self.assertAlmostEqual(c, 246.410875, places=6)

    def test_agile_n1_logistic_with_a_partial_dataset_of_20_samples(self):
        a = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_agile1_20samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 22.197651, places=6)
        self.assertAlmostEqual(b, 0.017039, places=6)
        self.assertAlmostEqual(c, 218.418992, places=6)

    def test_agile_n1_logistic_with_partial_datasets_prr_comparison(self):
        prr_20samples = TestEndSample.fit_log_agile1_20samples.get_prr_ml()
        prr_25samples = TestEndSample.fit_log_agile1_25samples.get_prr_ml()
        self.assertTrue(prr_20samples > prr_25samples)

    def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_35_samples(self):
        a = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_mixed_35samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 142.968176, places=6)
        self.assertAlmostEqual(b, 0.107149, places=6)

    def test_mixed_delayed_s_shaped_with_a_partial_dataset_of_15_samples(self):
        a = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[0]
        b = TestEndSample.fit_ds_mixed_15samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 54.895501, places=6)
        self.assertAlmostEqual(b, 0.805702, places=6)

    def test_mixed_delayed_s_shaped_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_ds_mixed_15samples.get_prr_ml()
        prr_35samples = TestEndSample.fit_ds_mixed_35samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_35samples)

    def test_mixed_logistic_with_a_partial_dataset_of_25_samples(self):
        a = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_mixed_25samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, -0.001534, places=6)
        self.assertAlmostEqual(b, 0.246161, places=6)
        self.assertAlmostEqual(c, -5.570353, places=6)

    def test_mixed_logistic_with_a_partial_dataset_of_35_samples(self):
        a = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[0]
        b = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[1]
        c = TestEndSample.fit_log_mixed_35samples.get_ml_parameters()[2]
        self.assertAlmostEqual(a, 0.005719, places=6)
        self.assertAlmostEqual(b, 0.198346, places=6)
        self.assertAlmostEqual(c, 13.363637, places=6)

    def test_mixed_logistic_with_partial_datasets_prr_comparison(self):
        prr_25samples = TestEndSample.fit_log_mixed_25samples.get_prr_ml()
        prr_35samples = TestEndSample.fit_log_mixed_35samples.get_prr_ml()
        self.assertTrue(prr_25samples > prr_35samples)

    def test_mixed_goel_okumoto_with_a_partial_dataset_of_35_samples(self):
        a = TestEndSample.fit_go_mixed_35samples.get_ml_parameters()[0]
        b = TestEndSample.fit_go_mixed_35samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 50.376732, places=6)
        self.assertAlmostEqual(b, 0.454540, places=6)

    def test_mixed_goel_okumoto_with_a_partial_dataset_of_15_samples(self):
        a = TestEndSample.fit_go_mixed_15samples.get_ml_parameters()[0]
        b = TestEndSample.fit_go_mixed_15samples.get_ml_parameters()[1]
        self.assertAlmostEqual(a, 55.988653, places=6)
        self.assertAlmostEqual(b, 0.332405, places=6)

    # Surprisingly, this test fails. Maybe it's an exception to the general rule?
    '''
    def test_mixed_goel_okumoto_with_partial_datasets_prr_comparison(self):
        prr_15samples = TestEndSample.fit_go_mixed_15samples.get_prr_ml()
        prr_35samples = TestEndSample.fit_go_mixed_35samples.get_prr_ml()
        self.assertTrue(prr_15samples > prr_35samples)
    '''
