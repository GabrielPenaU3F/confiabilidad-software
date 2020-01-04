import unittest

from src.domain.fitters.multistage_fitter import MultistageFitter
from src.exceptions.exceptions import InvalidStageDefinitionException


class TestMultistageStages(unittest.TestCase):

    full_go_fit = None
    ds_go_fit = None

    @classmethod
    def setUpClass(cls):
        cls.full_go_fit = cls.define_full_goel_okumoto_fit()
        cls.ds_go_fit = cls.define_ds_go_fit()

    @classmethod
    def define_full_goel_okumoto_fit(cls):
        multistage_fitter = MultistageFitter()
        multistage_fitter.add_stage(0, 250, 'goel-okumoto')
        return multistage_fitter.fit('ntds')

    @classmethod
    def define_ds_go_fit(cls):
        multistage_fitter = MultistageFitter()
        multistage_fitter.add_stage(0, 87, 'delayed-s-shaped')
        multistage_fitter.add_stage(87, 250, 'goel-okumoto')
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

    def test_multistage_fit_with_2_stages_has_2_stages(self):
        self.assertEqual(2, TestMultistageStages.ds_go_fit.get_number_of_stages())

    def test_ds_go_stage_1_begins_at_t_equal_0(self):
        stages = TestMultistageStages.ds_go_fit.get_stages()
        stage_1 = stages[0]
        self.assertEqual(0, stage_1.get_initial_t())

    def test_ds_go_stage_1_ends_at_t_equal_87(self):
        stages = TestMultistageStages.ds_go_fit.get_stages()
        stage_1 = stages[0]
        self.assertEqual(87, stage_1.get_end_t())

    def test_ds_go_stage_2_begins_at_t_equal_87(self):
        stages = TestMultistageStages.ds_go_fit.get_stages()
        stage_2 = stages[1]
        self.assertEqual(87, stage_2.get_initial_t())

    def test_ds_go_stage_2_ends_at_t_equal_250(self):
        stages = TestMultistageStages.ds_go_fit.get_stages()
        stage_2 = stages[1]
        self.assertEqual(250, stage_2.get_end_t())

    def test_ds_go_stage_2_begins_at_the_same_t_where_stage_1_ends(self):
        stages = TestMultistageStages.ds_go_fit.get_stages()
        stage_1 = stages[0]
        stage_2 = stages[1]
        self.assertEqual(stage_1.get_end_t(), stage_2.get_initial_t())

    def test_defining_a_stage_with_initial_time_different_than_previous_stage_end_time_should_raise_exception(self):
        with self.assertRaises(InvalidStageDefinitionException) as error:
            multistage_fitter = MultistageFitter()
            multistage_fitter.add_stage(0, 87, 'delayed-s-shaped')
            multistage_fitter.add_stage(90, 250, 'goel-okumoto')
        self.assertEqual(error.exception.strerror, 'The added stage must begin at the same t where the previous stage '
                                                   'ends')
