import unittest

from src.data.data_formater import TTFDataFormater
from src.data.data_repository import DataRepository


class TestTTFStageParameters(unittest.TestCase):

    ntds_data = None
    ttf_formater = None

    @classmethod
    def setUpClass(cls):
        cls.ntds_data = DataRepository.provide_project_data('ntds')
        cls.ttf_formater = TTFDataFormater.get_instance()

    def test_ttf_formater_determine_stage_t0_should_return_0_if_initial_t_is_0(self):
        t0 = self.ttf_formater.determine_stage_t0(self.ntds_data, 0)
        self.assertEqual(0, t0)

    def test_ttf_formater_determine_stage_t0_should_return_21_if_initial_t_is_32(self):
        t0 = self.ttf_formater.determine_stage_t0(self.ntds_data, 32)
        self.assertEqual(21, t0)

    def test_ttf_formater_determine_initial_sample_should_return_0_if_initial_t_is_0(self):
        initial_sample = self.ttf_formater.determine_stage_initial_sample(self.ntds_data, 0)
        self.assertEqual(0, initial_sample)

    def test_ttf_formater_determine_initial_sample_should_return_0_if_initial_t_is_9(self):
        initial_sample = self.ttf_formater.determine_stage_initial_sample(self.ntds_data, 9)
        self.assertEqual(0, initial_sample)

    def test_ttf_formater_determine_initial_sample_should_return_1_if_initial_t_is_11(self):
        initial_sample = self.ttf_formater.determine_stage_initial_sample(self.ntds_data, 11)
        self.assertEqual(1, initial_sample)

    def test_ttf_formater_determine_initial_sample_should_return_1_if_initial_t_is_21(self):
        initial_sample = self.ttf_formater.determine_stage_initial_sample(self.ntds_data, 21)
        self.assertEqual(1, initial_sample)

    def test_ttf_formater_determine_end_sample_should_return_2_if_end_t_is_32(self):
        end_sample = self.ttf_formater.determine_stage_end_sample(self.ntds_data, 32)
        self.assertEqual(2, end_sample)

    def test_ttf_formater_determine_end_sample_should_return_2_if_end_t_is_35(self):
        end_sample = self.ttf_formater.determine_stage_end_sample(self.ntds_data, 35)
        self.assertEqual(2, end_sample)

    def test_ttf_formater_determine_end_sample_should_return_25_if_end_t_is_260(self):
        end_sample = self.ttf_formater.determine_stage_end_sample(self.ntds_data, 250)
        self.assertEqual(25, end_sample)
