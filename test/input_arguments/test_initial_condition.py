import unittest

from src.domain.fitters.fitter import Fitter


class TestInitialCondition(unittest.TestCase):

    ttf_fit = None
    fpd_fit = None

    @classmethod
    def setUpClass(cls):
        #  x0 = 5 in ttf format means '0 failures reported at t=5'
        cls.ttf_fit = Fitter().fit('goel-okumoto', 'ntds', x0=5)
        #  x0 = 5 in fpd format means '5 failures were present at t=0'
        #cls.fpd_fit = Fitter().fit('goel-okumoto', 'mixed-waterfall-agile', x0=5)

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_x0_equal_5_is_27_comma_491544(self):
        a = TestInitialCondition.ttf_fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.590445, places=6)