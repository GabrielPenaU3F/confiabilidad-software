from abc import ABC


class FormatedData(ABC):

    formated_times = None
    original_times = None
    fpd = None
    cumulative_failures = None

    def get_cumulative_failures(self):
        return self.cumulative_failures

    def get_fpd(self):
        return self.fpd

    def get_formated_times(self):
        return self.formated_times

    def get_original_times(self):
        return self.original_times


class TTFFormatedData(FormatedData):

    def __init__(self, original_times, ttf, cumulative_failures):
        self.original_times = original_times
        self.formated_times = ttf
        self.fpd = None
        self.cumulative_failures = cumulative_failures


class FPDFormatedData(FormatedData):

    def __init__(self, original_times, formated_times, fpd, cumulative_failures):
        self.original_times = original_times
        self.formated_times = formated_times
        self.fpd = fpd
        self.cumulative_failures = cumulative_failures
