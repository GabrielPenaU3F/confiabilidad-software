import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestInitialCondition(unittest.TestCase):

    ttf_fit_ds = None
    fpd_fit_ds = None
    ttf_fit_go = None
    fpd_fit_go = None
    ttf_fit_log = None
    fpd_fit_log = None

    @classmethod
    def setUpClass(cls):
        cls.ttf_fit_ds = ModelFitter().fit('delayed-s-shaped', 'ntds', t0=5, mts=False)
        cls.fpd_fit_ds = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', t0=5, mts=False)
        cls.ttf_fit_go = ModelFitter().fit('goel-okumoto', 'ntds', t0=5, mts=False)
        cls.fpd_fit_go = ModelFitter().fit('goel-okumoto', 'mixed-waterfall-agile', t0=5, mts=False)
        cls.ttf_fit_log = ModelFitter().fit('logistic', 'ntds', t0=5, mts=False)
        cls.fpd_fit_log = ModelFitter().fit('logistic', 'mixed-waterfall-agile', t0=5, mts=False,
                                            initial_approx=(1000, 0.001, 100))

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_27_comma_572573(self):
        a = self.__class__.ttf_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.572573, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_018700(self):
        b = self.__class__.ttf_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018700, delta=10**(-6))

    def test_mixed_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_934_comma_422579(self):
        a = self.__class__.fpd_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 934.4225783, places=6)

    def test_mixed_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_023234(self):
        b = self.__class__.fpd_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023234, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_33_comma_529490(self):
        a = self.__class__.ttf_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.529490, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_006599(self):
        b = self.__class__.ttf_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.006599, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_1296_comma_800824(self):
        a = self.__class__.fpd_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1296.800824, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_004957(self):
        b = self.__class__.fpd_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005966, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_24_comma_640875(self):
        a = self.__class__.ttf_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_040930(self):
        b = self.__class__.ttf_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_76_comma_510170(self):
        c = self.__class__.ttf_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    def test_mixed_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_835_comma_529793(self):
        a = self.__class__.fpd_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 835.529793, places=6)

    def test_mixed_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_022703(self):
        b = self.__class__.fpd_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.022703, places=6)

    def test_mixed_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_90_comma_442185(self):
        c = self.__class__.fpd_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 90.442185, places=6)
