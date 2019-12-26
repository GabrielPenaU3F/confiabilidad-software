import unittest

import numpy as np

from src.domain.fitters.model_fitter import ModelFitter


class MTTFTest(unittest.TestCase):

    fit_ntds_go = None
    fit_mixed_ds = None
    fit_agile1_log = None
    fit_ntds_ds = None
    fit_ntds_log = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_go = ModelFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5))
        cls.fit_mixed_ds = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5))
        cls.fit_agile1_log = ModelFitter().fit('logistic', 'agile-n1', initial_approx=(100, 0.05, 20))
        cls.fit_ntds_ds = ModelFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5))
        cls.fit_ntds_log = ModelFitter().fit('logistic', 'ntds', initial_approx=(100, 0.05, 20))

    def test_ntds_data_goel_okumoto_mttf_is_non_decreasing(self):
        mttf = MTTFTest.fit_ntds_go.get_all_mttf()
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i-1]:
                decreasing = True
        self.assertFalse(decreasing)

    def test_mixed_data_delayed_s_shaped_mttf_is_non_decreasing(self):
        mttf = MTTFTest.fit_mixed_ds.get_all_mttf()
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i - 1]:
                decreasing = True
        self.assertFalse(decreasing)

    def test_agile1_data_logistic_mttf_is_non_decreasing(self):
        mttf = MTTFTest.fit_agile1_log.get_all_mttf()
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i-1]:
                decreasing = True
        self.assertFalse(decreasing)

    def test_ntds_data_goel_okumoto_mttf_1_is_5_comma_2397(self):
        mttf = MTTFTest.fit_ntds_go.get_mttf(1)
        self.assertAlmostEqual(5.2397, mttf, delta=0.0001)

    def test_agile1_data_log_mttf_10_is_202_comma_1979(self):
        mttf = MTTFTest.fit_agile1_log.get_mttf(10)
        self.assertAlmostEqual(208.1979, mttf, delta=0.0001)

    def test_mixed_data_delayed_s_shaped_mttf_does_not_contain_nan_on_the_first_100_failures(self):
        mttf = MTTFTest.fit_mixed_ds.get_all_mttf()
        nan = False
        for i in range(100):
            if np.isnan(mttf[i]):
                nan = True
        self.assertFalse(nan)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_1_is_14_comma_4(self):
        mttf = MTTFTest.fit_ntds_ds.get_mttf(1)
        self.assertAlmostEqual(mttf, 14.4, delta=0.1)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_2_is_22_comma_6(self):
        mttf = MTTFTest.fit_ntds_ds.get_mttf(2)
        self.assertAlmostEqual(mttf, 22.6, delta=0.1)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_3_is_29_comma_3(self):
        mttf = MTTFTest.fit_ntds_ds.get_mttf(3)
        self.assertAlmostEqual(mttf, 29.3, delta=0.1)

    def test_ntds_goel_okumoto_mttf_for_k_equal_1_is_5_comma_2(self):
        mttf = MTTFTest.fit_ntds_go.get_mttf(1)
        self.assertAlmostEqual(mttf, 5.2, delta=0.1)

    def test_ntds_goel_okumoto_mttf_for_k_equal_2_is_10_comma_6(self):
        mttf = MTTFTest.fit_ntds_go.get_mttf(2)
        self.assertAlmostEqual(mttf, 10.6, delta=0.1)

    def test_ntds_goel_okumoto_mttf_for_k_equal_3_is_16_comma_2(self):
        mttf = MTTFTest.fit_ntds_go.get_mttf(3)
        self.assertAlmostEqual(mttf, 16.2, delta=0.1)

    def test_ntds_logistic_mttf_for_k_equal_1_is_5_comma_5(self):
        mttf = MTTFTest.fit_ntds_log.get_mttf(1)
        self.assertAlmostEqual(mttf, 5.5, delta=0.1)

    def test_ntds_logistic_mttf_for_k_equal_2_is_15_comma_0(self):
        mttf = MTTFTest.fit_ntds_log.get_mttf(2)
        self.assertAlmostEqual(mttf, 15.0, delta=0.1)

    def test_ntds_logistic_mttf_for_k_equal_3_is_24_comma_9(self):
        mttf = MTTFTest.fit_ntds_log.get_mttf(3)
        self.assertAlmostEqual(mttf, 24.9, delta=0.1)
