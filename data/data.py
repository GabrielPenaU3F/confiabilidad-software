from abc import ABC, abstractmethod

import numpy as np


class Data(ABC):

    format = None
    data = None
    cumulative_failure = None

    def __init__(self, format, data):
        self.format = format
        self.data = data
        self.cumulative_failure = self.calculate_cumulative_failures(data)

    @abstractmethod
    def calculate_cumulative_failures(self, data):
        pass

    def get_cumulative_failures(self):
        return self.cumulative_failure

    def get_format(self):
        return self.format

    def get_data(self):
        return self.data


class NTDSData(Data):

    def __init__(self):
        format = 'ttf'
        data = [0, 9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                 104, 105, 116, 149, 156, 247, 249, 250]
        super().__init__(format, data)

    def calculate_cumulative_failures(self, data):
        return np.arange(0, len(data), 1)


class AgileN1Data(Data):

    def __init__(self):
        format = 'ttf'
        data = [0, 36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                 232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                 419, 439]
        super().__init__(format, data)

    def calculate_cumulative_failures(self, data):
        return np.arange(0, len(data), 1)


class MixedWaterfallAgileData(Data):

    def __init__(self):
        format = 'agrupados'
        data = [12, 22, 7, 3, 0, 1, 0, 0, 0, 3, 0, 0, 21, 5, 3, 1, 3, 0, 1, 2,
                 4, 1, 4, 1, 2, 4, 2, 2, 5, 3, 5, 2, 5, 2, 1, 7, 8, 3, 4, 27, 11, 12,
                 11, 8, 1, 3, 12, 1, 8, 6, 6, 3, 12, 17, 15, 18, 19, 16, 14, 8, 12,
                 11, 5, 6, 10, 1, 13, 10, 9, 7, 3, 7, 6, 6, 7, 9, 0, 8, 5, 8, 4, 2,
                 2, 2, 5, 3, 5, 1, 2, 0, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                 1, 3, 1, 3, 8, 2, 4, 7, 5, 3, 8, 7, 6, 2, 3, 6, 5, 5, 5, 1, 5, 1,
                 5, 3, 2, 5, 2, 5, 0, 3, 4, 2, 3, 1, 2, 1, 1, 0, 3, 1, 4, 3, 9, 1, 9,
                 1, 8, 6, 1, 4, 3, 5, 3, 0, 4, 5, 2, 0, 4, 1, 1, 1, 4, 6, 1, 5, 9,
                 1, 4, 5, 3, 3, 4, 5, 5, 2, 2, 3, 3, 5, 5, 5, 1, 3, 3, 0, 1, 3, 0, 1,
                 2, 2, 2, 1, 4, 2, 1, 0, 0, 2, 4, 2, 3, 1]
        super().__init__(format, data)

    def calculate_cumulative_failures(self, data):
        return np.cumsum(data)
