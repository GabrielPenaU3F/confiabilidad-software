import unittest

from src.data.data_formater import FPDDataFormater
from src.data.data_repository import DataRepository
from src.domain.optional_arguments import OptionalArguments


class TestFPDFitDataFormat(unittest.TestCase):

    mixed_data = None
    fpd_formater = None

    @classmethod
    def setUpClass(cls):
        cls.mixed_data = DataRepository.provide_project_data('mixed-waterfall-agile')
        cls.fpd_formater = FPDDataFormater.get_instance()

    def test_fpd_formater_should_return_the_original_times_of_the_mixed_dataset(self):
        optional_arguments = OptionalArguments()
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        original_times = formated_data.get_original_times()
        self.assertListEqual(self.mixed_data.get_times(), original_times)

    def test_fpd_formater_should_return_the_original_times_from_20_to_end(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 19})
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        original_times = formated_data.get_original_times()
        expected = self.mixed_data.get_times()[19:]
        self.assertListEqual(expected, original_times)

    def test_fpd_formater_should_return_the_original_times_from_20_to_40(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 19, 'end_sample': 39})
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        original_times = formated_data.get_original_times()
        expected = self.mixed_data.get_times()[19:40]
        self.assertListEqual(expected, original_times)

    def test_fpd_formater_should_format_the_times_with_a_0_at_its_beginning_if_t0_not_specified(self):
        optional_arguments = OptionalArguments()
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        formated_times = formated_data.get_formated_times()
        expected = [0] + self.mixed_data.get_times()
        self.assertListEqual(expected, formated_times)

    def test_fpd_formater_should_format_the_times_with_specified_t0_at_its_beginning(self):
        optional_arguments = OptionalArguments(**{'t0': 10})
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        formated_times = formated_data.get_formated_times()
        expected = [10] + self.mixed_data.get_times()
        self.assertListEqual(expected, formated_times)

    def test_fpd_formater_should_format_the_times_with_the_corresponding_t0_if_initial_sample_is_not_zero_and_t0_is_not_specified(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 19})
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        formated_times = formated_data.get_formated_times()
        expected = self.mixed_data.get_times()[18:len(self.mixed_data.get_times())]
        self.assertListEqual(expected, formated_times)

    def test_fpd_formater_should_return_the_cumulative_failures_of_the_dataset(self):
        optional_arguments = OptionalArguments()
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        expected = self.mixed_data.get_cumulative_failures()
        cumulative_failures = formated_data.get_cumulative_failures()
        self.assertListEqual(expected, cumulative_failures)

    def test_fpd_formater_should_return_the_cumulative_failures_from_20_to_40_when_specified_initial_and_end_samples(self):
        optional_arguments = OptionalArguments(**{'initial_sample': 19, 'end_sample': 39})
        formated_data = self.fpd_formater.give_format(self.mixed_data, optional_arguments)
        expected = self.mixed_data.get_cumulative_failures()[19:40]
        cumulative_failures = formated_data.get_cumulative_failures()
        self.assertListEqual(expected, cumulative_failures)
