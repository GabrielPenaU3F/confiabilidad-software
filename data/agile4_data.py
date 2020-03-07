from src.data.data import Data


class AgileN4Data(Data):

    def __init__(self):
        title = 'Agile #4'
        format = 'ttf'
        data = [57, 57, 57, 71, 113, 113, 113, 120, 132, 139,
                141, 141, 141, 142, 154, 156, 156, 169, 202, 204,
                216, 217, 237, 252, 282, 283, 302, 308, 311, 311,
                342, 377, 392, 399]
        super().__init__(title, format, data)
