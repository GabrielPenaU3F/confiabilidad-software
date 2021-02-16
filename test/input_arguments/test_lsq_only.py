import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestLSQOnly(unittest.TestCase):

    go_ntds_fit = None
    ds_ntds_fit = None
    log_ntds_fit = None

    @classmethod
    def setUpClass(cls):
        cls.go_ntds_fit = ModelFitter().fit('goel-okumoto', 'ntds', lsq_only=True)
        cls.ds_ntds_fit = ModelFitter().fit('delayed-s-shaped', 'ntds', lsq_only=True)
        cls.log_ntds_fit = ModelFitter().fit('logistic', 'ntds', lsq_only=True)

    def test_goel_okumoto_lsq_only_with_ntds_data_lsq_estimates_and_prr(self):
        a, b = self.__class__.go_ntds_fit.get_lsq_parameters()
        prr = self.__class__.go_ntds_fit.get_prr_lsq()
        self.assertAlmostEqual(a, 33.599461, places=6)
        self.assertAlmostEqual(b, 0.006296, places=6)
        self.assertAlmostEqual(prr, 1.507177, places=6)

    def test_goel_okumoto_lsq_only_ml_estimates_prr_and_aic_must_be_none(self):
        ml_params = self.__class__.go_ntds_fit.get_ml_parameters()
        prr = self.__class__.go_ntds_fit.get_prr_ml()
        aic = self.__class__.go_ntds_fit.get_aic()
        self.assertEqual(None, ml_params)
        self.assertEqual(None, prr)
        self.assertEqual(None, aic)

    def test_delayed_s_shaped_lsq_only_with_ntds_data_lsq_estimates_and_prr(self):
        a, b = self.__class__.ds_ntds_fit.get_lsq_parameters()
        prr = self.__class__.ds_ntds_fit.get_prr_lsq()
        self.assertAlmostEqual(a, 26.715480, places=6)
        self.assertAlmostEqual(b, 0.021213, places=6)
        self.assertAlmostEqual(prr, 2.044758, places=6)

    def test_delayed_s_shaped_lsq_only_ml_estimates_prr_and_aic_must_be_none(self):
        ml_params = self.__class__.ds_ntds_fit.get_ml_parameters()
        prr = self.__class__.ds_ntds_fit.get_prr_ml()
        aic = self.__class__.ds_ntds_fit.get_aic()
        self.assertEqual(None, ml_params)
        self.assertEqual(None, prr)
        self.assertEqual(None, aic)

    def test_logistic_lsq_only_with_ntds_data_lsq_estimates_and_prr(self):
        a, b, c = self.__class__.log_ntds_fit.get_lsq_parameters()
        prr = self.__class__.log_ntds_fit.get_prr_lsq()
        self.assertAlmostEqual(a, 24.640875, places=6)
        self.assertAlmostEqual(b, 0.040930, places=6)
        self.assertAlmostEqual(c, 76.510170, places=6)
        self.assertAlmostEqual(prr, 0.193478, places=6)

    def test_logistic_lsq_only_ml_estimates_prr_and_aic_must_be_none(self):
        ml_params = self.__class__.log_ntds_fit.get_ml_parameters()
        prr = self.__class__.log_ntds_fit.get_prr_ml()
        aic = self.__class__.log_ntds_fit.get_aic()
        self.assertEqual(None, ml_params)
        self.assertEqual(None, prr)
        self.assertEqual(None, aic)
