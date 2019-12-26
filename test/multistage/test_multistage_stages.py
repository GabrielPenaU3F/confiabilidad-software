import unittest

from src.domain.fitters.multistage_fitter import MultistageFitter


class TestMultistageStages(unittest.TestCase):

    full_go_fit = None

    @classmethod
    def setUpClass(cls):
        cls.full_go_fit = cls.define_full_goel_okumoto_fit()

    @classmethod
    def define_full_goel_okumoto_fit(cls):
        multistage_fitter = MultistageFitter()
        multistage_fitter.add_stage(0, 250, 'goel-okumoto')
        return multistage_fitter.fit('ntds')

    def test_multistage_fit_with_1_stage_has_only_1_stage(self):
        self.assertEqual(1, TestMultistageStages.full_go_fit.get_number_of_stages())

    def test_full_go_stage_1_begins_at_t_equal_0(self):
        stages = TestMultistageStages.full_go_fit.get_stages()
        stage_1 = stages[0]
        self.assertEqual(0, stage_1.get_initial_t())

    def test_full_go_stage_1_ends_at_t_equal_250(self):
        stages = TestMultistageStages.full_go_fit.get_stages()
        stage_1 = stages[0]
        self.assertEqual(250, stage_1.get_end_t())
