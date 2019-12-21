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

