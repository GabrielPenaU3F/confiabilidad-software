import unittest

from src.fitters.fitter import TTFFitter


class MTBFTest(unittest.TestCase):

    fit_ntds_go = None
    fit_ntds_ds = None
    fit_ntds_log = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_go = TTFFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5))
        cls.fit_ntds_ds = TTFFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5))
        cls.fit_ntds_log = TTFFitter().fit('logistic', 'ntds', initial_approx=(10, 0.05, 20))

    def test_ntds_goel_okumoto_mtbf_for_k_equal_1_is_5_comma_2(self):
        mtbf = MTBFTest.fit_ntds_go.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 5.2, delta=0.1)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_5_is_5_comma_9(self):
        mtbf = MTBFTest.fit_ntds_go.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.9, delta=0.1)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_20_is_13_comma_7(self):
        mtbf = MTBFTest.fit_ntds_go.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 13.7, delta=0.1)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_1_is_14_comma_4(self):
        mtbf = MTBFTest.fit_ntds_ds.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 14.4, delta=0.1)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_5_is_5_comma_8(self):
        mtbf = MTBFTest.fit_ntds_ds.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.8, delta=0.1)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_20_is_9_comma_0(self):
        mtbf = MTBFTest.fit_ntds_ds.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 9.0, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_1_is_5_comma_6(self):
        mtbf = MTBFTest.fit_ntds_log.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 5.6, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_5_is_7_comma_1(self):
        mtbf = MTBFTest.fit_ntds_log.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 7.1, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_20_is_4_comma_1(self):
        mtbf = MTBFTest.fit_ntds_log.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 4.1, delta=0.1)