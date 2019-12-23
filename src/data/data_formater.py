from abc import abstractmethod, ABC

import numpy as np

from src.data.formated_data import TTFFormatedData, FPDFormatedData
from src.exceptions.exceptions import InvalidArgumentException


class DataFormater(ABC):

    @abstractmethod
    def give_format(self, data, optional_arguments):
        pass

    def determine_end_sample(self, data, end_sample_arg):
        default_end_sample = len(data.get_data())
        if end_sample_arg > default_end_sample:
            raise InvalidArgumentException('The end sample must not exceed the length of the dataset')
        if end_sample_arg != 0:
            return end_sample_arg
        else:
            return default_end_sample


class TTFDataFormater(DataFormater):

    def give_format(self, data, optional_arguments):
        end = self.determine_end_sample(data, optional_arguments.get_end_sample())
        ttf_original_data = data.get_data()[0:end]
        cumulative_failures = data.get_cumulative_failures()[0:end + 1]
        t0 = optional_arguments.get_x0()
        ttf_formated = list(np.copy(ttf_original_data))
        ttf_formated.insert(0, t0)
        return TTFFormatedData(ttf_original_data, ttf_formated, cumulative_failures)


class FPDDataFormater(DataFormater):

    def give_format(self, data, optional_arguments):
        end = self.determine_end_sample(data, optional_arguments.get_end_sample())
        cumulative_failures = data.get_cumulative_failures()[0:end]

        y0 = optional_arguments.get_x0()
        cumulative_failures.insert(0, y0)
        fpd = list(np.copy(data.get_data()))
        original_times = data.get_times()[0:end]
        formated_times = list(np.copy(original_times))
        formated_times.insert(0, 0)

        return FPDFormatedData(original_times, formated_times, fpd, cumulative_failures)

