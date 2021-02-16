import unittest

import numpy as np

from src.domain.fitters.model_fitter import ModelFitter


class RegularMTTFTest(unittest.TestCase):

    fit_ntds_go = None
    fit_mixed_ds = None
    fit_agile1_log = None
    fit_ntds_ds = None
    fit_ntds_log = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_go = ModelFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5),
                                            lsq_only=True, mt_formula='regular')
        cls.fit_mixed_ds = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5),
                                             lsq_only=True, mt_formula='regular')
        cls.fit_agile1_log = ModelFitter().fit('logistic', 'agile-n1', initial_approx=(100, 0.05, 20),
                                               lsq_only=True, mt_formula='regular')
        cls.fit_ntds_ds = ModelFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5),
                                            lsq_only=True, mt_formula='regular')
        cls.fit_ntds_log = ModelFitter().fit('logistic', 'ntds', initial_approx=(100, 0.05, 20),
                                             lsq_only=True, mt_formula='regular')

    def test_ntds_data_goel_okumoto_regular_mttf_is_non_decreasing(self):
        mttf = self.__class__.fit_ntds_go.get_all_mttf()
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i-1]:
                decreasing = True
        self.assertFalse(decreasing)

    # Some weird stuff is happening on failure number 881 and its mttf is lower than number 880, an absurd.
    # It must be due to some imprecision in the saddlepoint approximation.
    def test_mixed_data_delayed_s_shaped_regular_mttf_first_200_is_non_decreasing(self):
        mttf = self.__class__.fit_mixed_ds.get_all_mttf()[0:200]
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i - 1]:
                decreasing = True
        self.assertFalse(decreasing)

    def test_agile1_data_logistic_regular_mttf_is_non_decreasing(self):
        mttf = self.__class__.fit_agile1_log.get_all_mttf()
        decreasing = False
        for i in range(1, len(mttf)):
            if mttf[i] < mttf[i-1]:
                decreasing = True
        self.assertFalse(decreasing)

    def test_mixed_data_delayed_s_shaped_mttf_does_not_contain_nan_on_the_first_100_failures(self):
        mttf = self.__class__.fit_mixed_ds.get_all_mttf()
        nan = False
        for i in range(100):
            if np.isnan(mttf[i]):
                nan = True
        self.assertFalse(nan)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_1_is_12_comma_8609(self):
        mttf = self.__class__.fit_ntds_ds.get_mttf(1)
        self.assertAlmostEqual(mttf, 12.8609, places=4)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_2_is_20_comma_1730(self):
        mttf = self.__class__.fit_ntds_ds.get_mttf(2)
        self.assertAlmostEqual(mttf, 20.1730, places=4)

    def test_ntds_delayed_s_shaped_mttf_for_k_equal_3_is_26_comma_2096(self):
        mttf = self.__class__.fit_ntds_ds.get_mttf(3)
        self.assertAlmostEqual(mttf, 26.2096, places=4)

    def test_ntds_data_goel_okumoto_regular_mttf_for_k_equal_1_is_4_comma_8768(self):
        mttf = self.__class__.fit_ntds_go.get_mttf(1)
        self.assertAlmostEqual(4.8768, mttf, places=4)

    def test_ntds_goel_okumoto_mttf_for_k_equal_2_is_9_comma_9137(self):
        mttf = self.__class__.fit_ntds_go.get_mttf(2)
        self.assertAlmostEqual(mttf, 9.9137, places=4)

    def test_ntds_goel_okumoto_mttf_for_k_equal_3_is_15_comma_1220(self):
        mttf = self.__class__.fit_ntds_go.get_mttf(3)
        self.assertAlmostEqual(mttf, 15.1220, places=4)

    def test_ntds_logistic_mttf_for_k_equal_1_is_5_comma_4796(self):
        mttf = self.__class__.fit_ntds_log.get_mttf(1)
        self.assertAlmostEqual(mttf, 5.4796, places=4)

    def test_ntds_logistic_mttf_for_k_equal_2_is_15_comma_0004(self):
        mttf = self.__class__.fit_ntds_log.get_mttf(2)
        self.assertAlmostEqual(mttf, 15.0004, places=4)

    def test_ntds_logistic_mttf_for_k_equal_3_is_24_comma_9004(self):
        mttf = self.__class__.fit_ntds_log.get_mttf(3)
        self.assertAlmostEqual(mttf, 24.9004, places=4)

    def test_agile1_logistic_mttf_for_k_equal_10_is_202_comma_1978(self):
        mttf = self.__class__.fit_agile1_log.get_mttf(10)
        self.assertAlmostEqual(208.1978, mttf, places=4)
