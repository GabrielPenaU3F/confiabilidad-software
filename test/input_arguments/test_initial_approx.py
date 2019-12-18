import unittest

from src.domain.fitters.fitter import Fitter


class TestInitialApprox(unittest.TestCase):

    # Using initial approx is already being tested on the 'models' test directory
    # Also, the default initial approx is the same as the one used on the other test set.
    # For a better testing, replace one or the other for a different p0=(a0, b0)

    def test_goel_okumoto_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('goel-okumoto', 'ntds')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 33.599359, places=6)
        self.assertAlmostEqual(b, 0.006296, places=6)

    def test_goel_okumoto_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('goel-okumoto', 'mixed-waterfall-agile')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 1416.913890, places=6)
        self.assertAlmostEqual(b, 0.004807, places=6)

    def test_delayed_s_shaped_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('delayed-s-shaped', 'ntds')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 26.715478, places=6)
        self.assertAlmostEqual(b, 0.021213, places=6)

    def test_delayed_s_shaped_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile')
        a, b = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 893.638883, places=6)
        self.assertAlmostEqual(b, 0.021788, places=6)

    def test_logistic_ttf_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('logistic', 'ntds')
        a, b, c = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 24.611413, places=6)
        self.assertAlmostEqual(b, 0.041331, places=6)
        self.assertAlmostEqual(c, 76.485839, places=6)

    def test_logistic_grouped_fpd_without_initial_approx_should_take_the_default_initial_approx(self):
        fit = Fitter().fit('logistic', 'mixed-waterfall-agile')
        a, b, c = fit.get_lsq_parameters()
        self.assertAlmostEqual(a, 835.410586, places=6)
        self.assertAlmostEqual(b, 0.030741, places=6)
        self.assertAlmostEqual(c, 75.801125, places=6)

