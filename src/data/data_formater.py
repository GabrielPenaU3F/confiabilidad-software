from abc import abstractmethod, ABC

import numpy as np

from src.data.formated_data import TTFFormatedData, FPDFormatedData
from src.exceptions.exceptions import InvalidArgumentException


class DataFormater(ABC):

    singleton = None

    @abstractmethod
    def give_format(self, data, optional_arguments):
        pass

    def determine_end_sample(self, data, end_sample_arg):
        default_end_sample = len(data.get_data())
        if end_sample_arg + 1 > default_end_sample:
            raise InvalidArgumentException('The end sample must not exceed the length of the dataset')
        if 0 < end_sample_arg < default_end_sample:
            return end_sample_arg + 1
        else:
            return default_end_sample

    def determine_initial_sample(self, data, initial_sample_arg):
        default_initial_sample = 0
        n = len(data.get_data())
        if 0 < initial_sample_arg < n - 1:
            return initial_sample_arg
        elif initial_sample_arg >= n:
            raise InvalidArgumentException('The initial sample must not exceed the length of the dataset')
        else:
            return default_initial_sample

    def determine_t0(self, times, t0_arg, start):
        t0 = 0
        if t0_arg > t0:
            t0 = t0_arg
        elif start > 0:
            t0 = times[start - 1]
        return t0

    def determine_format_parameters(self, data, optional_arguments):
        start = self.determine_initial_sample(data, optional_arguments.get_initial_sample())
        end = self.determine_end_sample(data, optional_arguments.get_end_sample())
        t0 = self.determine_t0(data.get_times(), optional_arguments.get_t0(), start)
        return start, end, t0

    def format_times(self, times, t0):
        formated_times = list(np.copy(times))
        formated_times.insert(0, t0)
        return formated_times

    def determine_stage_end_sample(self, data, end_t):
        times = data.get_times()
        for i in range(len(times)):
            if times[i] > end_t:
                return i - 1
        return len(times) - 1

    def determine_stage_initial_sample(self, data, initial_t):
        times = data.get_times()
        for i in range(len(times)):
            if times[i] >= initial_t:
                return i

    def determine_stage_t0(self, data, initial_t):
        times = list(np.copy(data.get_times()))
        times.insert(0, 0)
        for i in range(1, len(times)):
            if times[i] >= initial_t:
                return times[i - 1]

    @classmethod
    def slice_data(cls, start, end, *data_arrays):
        sliced = []
        for data in data_arrays:
            if end == 0:
                sliced.append(list(np.copy(data))[start:])
            else:
                sliced.append(list(np.copy(data))[start:end])
        return sliced


class TTFDataFormater(DataFormater):

    @classmethod
    def get_instance(cls):
        if cls.singleton is None:
            cls.singleton = TTFDataFormater()
        return cls.singleton

    def give_format(self, data, optional_arguments):
        start, end, t0 = self.determine_format_parameters(data, optional_arguments)
        sliced_ttf_original_data, sliced_cumulative_failures = DataFormater.\
            slice_data(start, end, data.get_data(), data.get_cumulative_failures())
        formated_ttf = self.format_times(sliced_ttf_original_data, t0)
        return TTFFormatedData(sliced_ttf_original_data, formated_ttf, sliced_cumulative_failures)

    def determine_stage_end_sample(self, data, end_t):
        ttfs = data.get_data()
        for i in range(len(ttfs)):
            if ttfs[i] > end_t:
                return i - 1
        return len(ttfs) - 1


class FPDDataFormater(DataFormater):

    @classmethod
    def get_instance(cls):
        if cls.singleton is None:
            cls.singleton = FPDDataFormater()
        return cls.singleton

    def give_format(self, data, optional_arguments):
        start, end, t0 = self.determine_format_parameters(data, optional_arguments)
        sliced_original_times, sliced_cumulative_failures, sliced_fpd = DataFormater.\
            slice_data(start, end, data.get_times(), data.get_cumulative_failures(), data.get_data())
        formated_times = self.format_times(sliced_original_times, t0)
        return FPDFormatedData(sliced_original_times, formated_times, sliced_fpd, sliced_cumulative_failures)
