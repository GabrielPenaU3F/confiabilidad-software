from src.data.data import Data


class MixedWaterfallAgileData(Data):

    def __init__(self):
        title = 'Mixed Waterfall-Agile'
        format = 'grouped'
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
        super().__init__(title, format, data)