from abc import ABC


class FormatedData(ABC):

    times = None
    cumulative_failures = None

    def get_cumulative_failures(self):
        return self.cumulative_failures

    def get_times(self):
        return self.times


class TTFFormatedData(FormatedData):

    def __init__(self, ttf, cumulative_failures):
        self.times = ttf
        self.cumulative_failures = cumulative_failures
