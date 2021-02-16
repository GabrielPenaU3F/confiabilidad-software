import unittest

from src.domain.fitters.model_fitter import ModelFitter


class ConditionalMTBFTest(unittest.TestCase):

    fit_ntds_bc = None

    @classmethod
    def setUpClass(cls):
        cls.fit_ntds_bc = ModelFitter().fit('barraza-contagion', 'ntds', initial_approx=(10, 0.01),
                                            lsq_only=True, mt_formula='conditional')

    def test_ntds_bc_mtbf_for_k_equal_1_is_18_comma_0343(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 18.0343, places=4)

    def test_ntds_bc_mtbf_for_k_equal_5_is_14_comma_1492(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 14.1492, places=4)

    def test_ntds_bc_mtbf_for_k_equal_20_is_8_comma_3433(self):
        mtbf = self.__class__.fit_ntds_bc.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 8.3433, places=4)
