import unittest

from src.domain.fitters.multistage_fitter import MultistageFitter
from src.exceptions.exceptions import InvalidFitException


class TestNTDSMultistageFit(unittest.TestCase):

    ds_go_fit = None

    @classmethod
    def setUpClass(cls):
        cls.define_ds_go_fit()

    @classmethod
    def define_ds_go_fit(cls):
        ds_go_fitter = MultistageFitter()
        ds_go_fitter.add_stage(0, 98, 'delayed-s-shaped')
        ds_go_fitter.add_stage(98, 250, 'goel-okumoto')
        cls.ds_go_fit = ds_go_fitter.fit('ntds')

    def define_invalid_ds_go_fit(self):
        ds_go_fitter = MultistageFitter()
        ds_go_fitter.add_stage(0, 87, 'delayed-s-shaped')
        ds_go_fitter.add_stage(87, 250, 'goel-okumoto')
        ds_go_fitter.fit('ntds')

    def test_ds_go_stage_1_a_parameter_should_be_52_comma_069508(self):
        stages = TestNTDSMultistageFit.ds_go_fit.get_stages()
        ds_stage = stages[0]
        a = ds_stage.get_ml_params()[0]
        self.assertAlmostEqual(52.069508, a, places=6)

    def test_ds_go_stage_1_b_parameter_should_be_0_comma_012068(self):
        stages = TestNTDSMultistageFit.ds_go_fit.get_stages()
        ds_stage = stages[0]
        b = ds_stage.get_ml_params()[1]
        self.assertAlmostEqual(0.012068, b, places=6)

    def test_ds_go_invalid_fit_should_raise_exception_if_a_negative_parameter_is_returned(self):
        with self.assertRaises(InvalidFitException) as error:
            self.define_invalid_ds_go_fit()
        self.assertEqual(error.exception.strerror,
                         'Stage 1: ML equations returned an invalid solution. Try a different initial approximation')
