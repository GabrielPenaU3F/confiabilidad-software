import unittest

from src.data.data_formater import TTFDataFormater
from src.data.data_repository import DataRepository
from src.domain.optional_arguments import OptionalArguments


class TestTTFFitDataFormat(unittest.TestCase):

    ntds_data = None
    ttf_formater = None

    @classmethod
    def setUpClass(cls):
        cls.ntds_data = DataRepository.provide_project_data('ntds')
        cls.ttf_formater = TTFDataFormater.get_instance()

    def test_ttf_formater_should_return_the_original_ttfs(self):
        optional_arguments = OptionalArguments()
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        self.assertListEqual(self.ntds_data.get_data(), original_ttf)

    def test_ttf_formater_should_return_the_original_ttfs_from_87_to_250(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        expected = self.ntds_data.get_data()[13:]
        self.assertListEqual(expected, original_ttf)

    def test_ttf_formater_should_return_the_original_ttfs_from_87_to_250_when_specifying_end_sample(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13, 'end_sample': 25})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        original_ttf = formated_data.get_original_times()
        expected = self.ntds_data.get_data()[13:]
        self.assertListEqual(expected, original_ttf)

    def test_ttf_formater_should_format_the_ttfs_with_a_0_at_its_beginning_if_t0_not_specified(self):
        optional_arguments = OptionalArguments()
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [0] + self.ntds_data.get_data()
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_format_the_ttfs_with_specified_t0_at_its_beginning(self):
        optional_arguments = OptionalArguments(**{'t0': 10})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [10] + self.ntds_data.get_data()
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_format_the_ttfs_with_the_corresponding_t0_if_initial_sample_is_not_zero_and_t0_is_not_specified(
            self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = self.ntds_data.get_data()[12:]
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_return_the_ttfs_from_87_to_250_with_specified_t0_at_its_beginning(self):
        optional_arguments = OptionalArguments(**{'t0': 10, 'initial_sample': 13, 'end_sample': 25})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        formated_ttf = formated_data.get_formated_times()
        expected = [10] + self.ntds_data.get_data()[13:]
        self.assertListEqual(expected, formated_ttf)

    def test_ttf_formater_should_return_the_cumulative_failures_of_the_dataset(self):
        optional_arguments = OptionalArguments()
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        expected = list(range(1, len(self.ntds_data.get_data()) + 1))
        cumulative_failures = formated_data.get_cumulative_failures()
        self.assertListEqual(expected, cumulative_failures)

    def test_ttf_formater_should_return_the_cumulative_failures_from_13_to_25_when_specified_initial_and_end_samples(
            self):
        optional_arguments = OptionalArguments(**{'initial_sample': 13, 'end_sample': 25})
        formated_data = self.ttf_formater.give_format(self.ntds_data, optional_arguments)
        expected = list(range(14, len(self.ntds_data.get_data()) + 1))
        cumulative_failures = formated_data.get_cumulative_failures()
        self.assertListEqual(expected, cumulative_failures)