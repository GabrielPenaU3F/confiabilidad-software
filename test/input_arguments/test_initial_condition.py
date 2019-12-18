import unittest

from src.domain.fitters.fitter import TTFFitter, GroupedFPDFitter


class TestInitialCondition(unittest.TestCase):

    ttf_fit = None

    @classmethod
    def setUpClass(cls):
        #  x0 = 5 means '0 failures reported at t=5'
        cls.ttf_fit = TTFFitter().fit('goel-okumoto', 'ntds', x0=5)
        #  x0 = 5 means '5 failures were present at t=0'
        cls.grouped_fit = GroupedFPDFitter().fit('goel-okumoto', 'mixed-waterfall-agile', x0=5)

    def test_initial_k_of_ttf_fit_is_5(self):
        times = TestInitialCondition.ttf_fit.get_times()
        x0 = times[0]
        self.assertEqual(5, x0)
