import unittest

from src.domain.fitters.model_fitter import ModelFitter


class TestInitialApprox(unittest.TestCase):

    # Using initial approx is already being tested on the 'models' test directory
    # Also, the default initial approx is the same as the one used on the other test set.
    # For a better testing, replace one or the other for a different p0=(a0, b0)

    def test_goel_okumoto_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('goel-okumoto', 'ntds')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 33.599461, places=6)
        self.assertAlmostEqual(b, 0.006296, places=6)

    def test_goel_okumoto_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('goel-okumoto', 'mixed-waterfall-agile')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 1416.915295, places=6)
        self.assertAlmostEqual(b, 0.004807, places=6)

    def test_delayed_s_shaped_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('delayed-s-shaped', 'ntds')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 26.715480, places=6)
        self.assertAlmostEqual(b, 0.021213, places=6)

    def test_delayed_s_shaped_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 893.639700, places=6)
        self.assertAlmostEqual(b, 0.021788, places=6)

    def test_logistic_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('logistic', 'ntds')
        a, b, c = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 24.640875, places=6)
        self.assertAlmostEqual(b, 0.040930, places=6)
        self.assertAlmostEqual(c, 76.510170, places=6)

    def test_logistic_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = ModelFitter().fit('logistic', 'mixed-waterfall-agile')
        a, b, c = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 835.410477, places=6)
        self.assertAlmostEqual(b, 0.030741, places=6)
        self.assertAlmostEqual(c, 75.801110, places=6)

