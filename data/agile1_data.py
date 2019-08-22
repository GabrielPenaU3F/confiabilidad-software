from src.data.data import Data


class AgileN1Data(Data):

    def __init__(self):
        title = 'Agile #1'
        format = 'ttf'
        data = [36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                419, 439]
        super().__init__(title, format, data)
