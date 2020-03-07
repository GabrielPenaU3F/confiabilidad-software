from src.data.data import Data


class AgileN3Data(Data):

    def __init__(self):
        title = 'Agile #3'
        format = 'ttf'
        data = [55, 68, 70, 76, 80, 81, 81, 81, 81, 87,
                88, 96, 98, 98, 108, 110, 110, 116, 117, 118,
                124, 133, 138, 139, 139, 139, 139, 140, 143, 144,
                145, 146, 147, 150, 150, 150, 150, 150, 150, 151,
                157, 158, 158, 158, 161, 179, 200, 203, 203, 207,
                208, 220, 235, 255, 258, 280, 280, 285, 285, 287,
                291, 297, 301]
        super().__init__(title, format, data)
