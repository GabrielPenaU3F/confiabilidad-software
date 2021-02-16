import unittest

from src.domain.fitters.model_fitter import ModelFitter


class RegularMTBFTest(unittest.TestCase):

    fit_ntds_go = None
    fit_ntds_ds = None
    fit_ntds_log = None
    fit_ntds_bc = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_go = ModelFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5),
                                            lsq_only=True, mt_formula='regular')
        cls.fit_ntds_ds = ModelFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5),
                                            lsq_only=True, mt_formula='regular')
        cls.fit_ntds_log = ModelFitter().fit('logistic', 'ntds', initial_approx=(10, 0.05, 20),
                                             lsq_only=True, mt_formula='regular')
        cls.fit_ntds_bc = ModelFitter().fit('barraza-contagion', 'ntds', initial_approx=(10, 0.01),
                                            lsq_only=True, mt_formula='regular')

    def test_ntds_goel_okumoto_mtbf_for_k_equal_1_is_4_comma_8768(self):
        mtbf = self.__class__.fit_ntds_go.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 4.8768, places=4)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_5_is_5_comma_5907(self):
        mtbf = self.__class__.fit_ntds_go.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.5907, places=4)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_20_is_12_comma_9712(self):
        mtbf = self.__class__.fit_ntds_go.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 12.9712, places=4)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_1_is_12_comma_8609(self):
        mtbf = self.__class__.fit_ntds_ds.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 12.8609, places=4)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_5_is_5_comma_1881(self):
        mtbf = self.__class__.fit_ntds_ds.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.1881, places=4)

    def test_ntds_delayed_s_shaped_mtbf_for_k_equal_20_is_8_comma_0690(self):
        mtbf = self.__class__.fit_ntds_ds.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 8.06799, places=4)

    def test_ntds_logistic_mtbf_for_k_equal_1_is_5_comma_4796(self):
        mtbf = self.__class__.fit_ntds_log.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 5.4796, places=4)

    def test_ntds_logistic_mtbf_for_k_equal_5_is_7_comma_2390(self):
        mtbf = self.__class__.fit_ntds_log.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 7.2390, places=4)

    def test_ntds_logistic_mtbf_for_k_equal_20_is_4_comma_2093(self):
        mtbf = self.__class__.fit_ntds_log.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 4.2093, places=4)

    def test_bc_mtbf_for_k_equal_1_with_regular_mtbf_formula_is_2_comma_6691(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 2.6691, places=4)

    def test_bc_mtbf_for_k_equal_5_with_regular_mtbf_formula_is_5_comma_5458(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.5458, places=4)

    def test_bc_mtbf_for_k_equal_20_with_regular_mtbf_formula_is_11_comma_0418(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 11.0418, places=4)

