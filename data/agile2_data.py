from src.data.data import Data


class AgileN2Data(Data):

    def __init__(self):
        title = 'Agile #2'
        format = 'grouped'
        data = [15, 14, 5, 4, 39, 24, 25, 35, 26, 38, 34]
        times = [1, 103, 121, 151, 248, 480, 561, 609, 663, 691, 974]
        super().__init__(title, format, data, times=times)
