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
        #  t0 = 5 in ttf format means '0 failures reported at t=5'
        #  t0 = 5 in fpd format means 'the dataset begins at t=6'
        cls.ttf_fit_ds = ModelFitter().fit('delayed-s-shaped', 'ntds', t0=5)
        # cls.fpd_fit_ds = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_go = ModelFitter().fit('goel-okumoto', 'ntds', t0=5)
        # cls.fpd_fit_go = ModelFitter().fit('goel-okumoto', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_log = ModelFitter().fit('logistic', 'ntds', t0=5)
        # cls.fpd_fit_log = ModelFitter().fit('logistic', 'mixed-waterfall-agile', t0=5)

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_27_comma_572573(self):
        a = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.572573, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_018700(self):
        b = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018700, delta=10**(-6))

    def test_mixed_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_940_comma_279403(self):
        a = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 940.279403, places=6)

    def test_mixed_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_021931(self):
        b = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.021931, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_33_comma_529490(self):
        a = TestInitialCondition.ttf_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.529490, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_006599(self):
        b = TestInitialCondition.ttf_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.006599, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_1414_comma_278491(self):
        a = TestInitialCondition.fpd_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1407.755657, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_004957(self):
        b = TestInitialCondition.fpd_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.004957, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_24_comma_640875(self):
        a = TestInitialCondition.ttf_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_040930(self):
        b = TestInitialCondition.ttf_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_76_comma_510170(self):
        c = TestInitialCondition.ttf_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    def test_mixed_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_835_comma_496030(self):
        a = TestInitialCondition.fpd_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 835.496030, places=6)

    def test_mixed_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_022954(self):
        b = TestInitialCondition.fpd_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.022954, places=6)

    def test_mixed_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_94_comma_590177(self):
        c = TestInitialCondition.fpd_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 94.590177, places=6)
