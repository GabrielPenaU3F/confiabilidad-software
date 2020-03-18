import numpy as np


class Data:

    title = None
    format = None
    data = None
    cumulative_failures = None
    times = None
    project_id = None

    def __init__(self, title, format, data, **kwargs):
        self.title = title
        self.format = format
        self.data = data
        self.times = kwargs.get('times')
        self.project_id = kwargs.get('project_id')
        self.cumulative_failures = self.calculate_cumulative_failures(data)

    def calculate_cumulative_failures(self, data):
        if self.format == 'ttf':
            return list(np.arange(1, len(data) + 1))
        elif self.format == 'fpd':
            return list(np.cumsum(data))

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
            return list(self.data)
        elif self.format == 'fpd':
            if self.times is None:
                return list(np.arange(1, len(self.data) + 1))
            return self.times

    def get_project_id(self):
        return self.project_id

    def get_time_between_failures(self):
        tbfs = [self.data[0]]
        if self.format == 'ttf':
            for i in range(1, len(self.data)):
                tbfs.append(self.data[i] - self.data[i-1])
        return tbfs
