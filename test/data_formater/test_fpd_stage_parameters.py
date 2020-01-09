import unittest

from src.data.data_formater import FPDDataFormater
from src.data.data_repository import DataRepository


class TestFPDStageParameters(unittest.TestCase):

    mixed_data = None
    fpd_formater = None

    @classmethod
    def setUpClass(cls):
        cls.mixed_data = DataRepository.provide_project_data('mixed-waterfall-agile')
        cls.fpd_formater = FPDDataFormater.get_instance()

    def test_fpd_formater_determine_stage_t0_should_return_0_if_initial_t_is_0(self):
        t0 = self.fpd_formater.determine_stage_t0(self.mixed_data, 0)
        self.assertEqual(0, t0)

    def test_fpd_formater_determine_stage_t0_should_return_0_if_initial_t_is_1(self):
        t0 = self.fpd_formater.determine_stage_t0(self.mixed_data, 1)
        self.assertEqual(0, t0)

    def test_fpd_formater_determine_stage_t0_should_return_5_if_initial_t_is_6(self):
        t0 = self.fpd_formater.determine_stage_t0(self.mixed_data, 6)
        self.assertEqual(5, t0)

    def test_fpd_formater_determine_initial_sample_should_return_0_if_initial_t_is_0(self):
        initial_sample = self.fpd_formater.determine_stage_initial_sample(self.mixed_data, 0)
        self.assertEqual(0, initial_sample)

    def test_fpd_formater_determine_initial_sample_should_return_0_if_initial_t_is_1(self):
        initial_sample = self.fpd_formater.determine_stage_initial_sample(self.mixed_data, 1)
        self.assertEqual(0, initial_sample)

    def test_fpd_formater_determine_initial_sample_should_return_10_if_initial_t_is_11(self):
        initial_sample = self.fpd_formater.determine_stage_initial_sample(self.mixed_data, 11)
        self.assertEqual(10, initial_sample)

    def test_fpd_formater_determine_end_sample_should_return_2_if_end_t_is_3(self):
        end_sample = self.fpd_formater.determine_stage_end_sample(self.mixed_data, 3)
        self.assertEqual(2, end_sample)

    def test_fpd_formater_determine_end_sample_should_return_208_if_end_t_is_209(self):
        end_sample = self.fpd_formater.determine_stage_end_sample(self.mixed_data, 209)
        self.assertEqual(208, end_sample)
