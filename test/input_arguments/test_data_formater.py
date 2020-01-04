import unittest

from src.data.data_formater import TTFDataFormater
from src.data.data_repository import DataRepository
from src.domain.fitters.optional_arguments import OptionalArguments


class TestDataFormater(unittest.TestCase):

    ntds_ttfs = [9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                 104, 105, 116, 149, 156, 247, 249, 250]
    data = None
    formater = None

    @classmethod
    def setUpClass(cls):
        cls.data = DataRepository.provide_project_data('ntds')
        cls.formater = TTFDataFormater.get_instance()

    def test_ttf_formater_should_return_the_original_ttfs_of_the_ntds_dataset(self):
        optional_arguments = OptionalArguments()
        formated_data = self.formater.give_format(self.data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        self.assertListEqual(self.ntds_ttfs, original_ttf)

    def test_ttf_formater_should_return_the_original_ttfs_of_the_ntds_dataset_from_87_to_250(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13})
        formated_data = self.formater.give_format(self.data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        expected = self.ntds_ttfs[13:len(self.ntds_ttfs)]
        self.assertListEqual(expected, original_ttf)

    def test_ttf_formater_should_return_the_original_ttfs_of_the_ntds_dataset_from_87_to_250_when_specifying_end_sample(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13, 'end_sample': 25})
        formated_data = self.formater.give_format(self.data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        expected = self.ntds_ttfs[13:len(self.ntds_ttfs)]
        self.assertListEqual(expected, original_ttf)

    def test_ttf_formater_should_return_the_ttfs_of_the_ntds_dataset_with_a_0_at_its_beginning_if_t0_not_specified(self):
        optional_arguments = OptionalArguments()
        formated_data = self.formater.give_format(self.data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [0] + self.ntds_ttfs
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_return_the_ttfs_of_the_ntds_dataset_with_specified_t0_at_its_beginning(self):
        optional_arguments = OptionalArguments(**{'t0': 10})
        formated_data = self.formater.give_format(self.data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [10] + self.ntds_ttfs
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_return_the_ttfs_of_the_ntds_dataset_from_87_to_250_with_specified_t0_at_its_beginning(self):
        optional_arguments = OptionalArguments(**{'t0': 10, 'initial_sample': 13, 'end_sample': 25})
        formated_data = self.formater.give_format(self.data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [10] + self.ntds_ttfs[13:len(self.ntds_ttfs)]
        self.assertListEqual(expected, formated_ttf)
