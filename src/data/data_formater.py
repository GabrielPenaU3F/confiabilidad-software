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

    def determine_initial_sample(self, data, initial_sample_arg):
        default_initial_sample = 0
        n = len(data.get_data())
        if 0 < initial_sample_arg < n - 1:
            return initial_sample_arg - 1
        elif initial_sample_arg > n:
            raise InvalidArgumentException('The initial sample must not exceed the length of the dataset')
        else:
            return default_initial_sample


class TTFDataFormater(DataFormater):

    def give_format(self, data, optional_arguments):
        start = self.determine_initial_sample(data, optional_arguments.get_initial_sample())
        end = self.determine_end_sample(data, optional_arguments.get_end_sample())
        ttf_original_data = data.get_data()[start:end]
        cumulative_failures = data.get_cumulative_failures()[start + 1:end + 1]
        t0 = optional_arguments.get_t0()
        formated_ttf = list(np.copy(ttf_original_data))
        initial_t = self.determine_initial_t(data.get_data(), start)
        formated_ttf.insert(0, initial_t)
        for i in range(len(formated_ttf)):
            formated_ttf[i] = formated_ttf[i] + t0
        return TTFFormatedData(ttf_original_data, formated_ttf, cumulative_failures)

    def determine_initial_t(self, ttf, start):
        if start == 0:
            return 0
        elif start > 0:
            return ttf[start - 1]


class FPDDataFormater(DataFormater):

    def give_format(self, data, optional_arguments):
        start = self.determine_initial_sample(data, optional_arguments.get_initial_sample())
        end = self.determine_end_sample(data, optional_arguments.get_end_sample())
        cumulative_failures = data.get_cumulative_failures()[start:end]
        fpd = list(np.copy(data.get_data()[start:end]))
        original_times = data.get_times()[start:end]
        formated_times = list(np.copy(original_times))
        t0 = optional_arguments.get_t0()
        formated_times.insert(0, t0)
        for i in range(1, len(formated_times)):
            formated_times[i] = original_times[i - 1] + t0

        return FPDFormatedData(original_times, formated_times, fpd, cumulative_failures)

