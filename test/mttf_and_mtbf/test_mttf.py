import unittest

import numpy as np

from src.fitters.fitter import TTFFitter, GroupedFPDFitter


class MTTFTest(unittest.TestCase):

    fit_ntds_go = None
    fit_mixed_ds = None
    fit_agile1_log = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_go = TTFFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5))
        cls.fit_mixed_ds = GroupedFPDFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5))
        cls.fit_agile1_log = TTFFitter().fit('logistic', 'agile-n1')

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

    def test_agile1_data_log_mttf_10_is_202_comma_6267(self):
        mttf = MTTFTest.fit_agile1_log.get_mttf(10)
        self.assertAlmostEqual(208.6267, mttf, delta=0.0001)

    def test_mixed_data_delayed_s_shaped_mttf_does_not_contain_nan_on_the_first_100_failures(self):
        mttf = MTTFTest.fit_mixed_ds.get_all_mttf()
        nan = False
        for i in range(100):
            if np.isnan(mttf[i]):
                nan = True
        self.assertFalse(nan)
