from abc import ABC

import numpy as np


class Data(ABC):

    title = None
    format = None
    data = None
    cumulative_failures = None

    def __init__(self, title, format, data):
        self.title = title
        self.format = format
        self.data = data
        self.cumulative_failures = self.calculate_cumulative_failures(data)

    def calculate_cumulative_failures(self, data):
        # It begins on 0, result including '0 faults at t=0'
        if self.format == 'ttf':
            return np.arange(0, len(data) + 1, 1)
        elif self.format == 'grouped':
            return np.cumsum(data)

    def get_cumulative_failures(self):
        return self.cumulative_failures

    def get_format(self):
        return self.format

    def get_data(self):
        return self.data

    def get_project_title(self):
        return self.title

    def get_times(self):
        if self.format == 'ttf':
            return [0] + self.data
        elif self.format == 'grouped':
            return np.arange(1, len(self.data) + 1)