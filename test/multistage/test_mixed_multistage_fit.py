import unittest

from src.domain.fitters.multistage_fitter import MultistageFitter


class TestMixedMultistageFit(unittest.TestCase):
    
    log_mo_fit = None

    @classmethod
    def setUpClass(cls):
        cls.define_log_mo_fit()

    @classmethod
    def define_log_mo_fit(cls):
        log_mo_fitter = MultistageFitter()
        log_mo_fitter.add_stage(0, 110, 'logistic', initial_approx=(800, 0.001, 100))
        log_mo_fitter.add_stage(110, 209, 'musa-okumoto', initial_approx=(90, 0.001))
        cls.log_mo_fit = log_mo_fitter.fit('mixed-waterfall-agile')

    def test_log_mo_stage_1_a_parameter_should_be_622_comma_975985(self):
        stages = self.log_mo_fit.get_stages()
        log_stage = stages[0]
        a = log_stage.get_ml_params()[0]
        self.assertAlmostEqual(622.975985, a, places=6)

    def test_log_mo_stage_1_b_parameter_should_be_0_comma_058741(self):
        stages = self.log_mo_fit.get_stages()
        log_stage = stages[0]
        b = log_stage.get_ml_params()[1]
        self.assertAlmostEqual(0.058741, b, places=6)

    def test_log_mo_stage_1_c_parameter_should_be_52_comma_127784(self):
        stages = self.log_mo_fit.get_stages()
        log_stage = stages[0]
        c = log_stage.get_ml_params()[2]
        self.assertAlmostEqual(52.127784, c, places=6)

    def test_log_mo_stage_2_a_parameter_should_be_848_comma_649606(self):
        stages = self.log_mo_fit.get_stages()
        mo_stage = stages[1]
        a = mo_stage.get_ml_params()[0]
        self.assertAlmostEqual(848.649606, a, places=6)

    def test_log_mo_stage_2_b_parameter_should_be_0_comma_009115(self):
        stages = self.log_mo_fit.get_stages()
        mo_stage = stages[1]
        b = mo_stage.get_ml_params()[1]
        self.assertAlmostEqual(0.009115, b, places=6)
