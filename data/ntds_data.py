from src.data.data import Data


class NTDSData(Data):

    def __init__(self):
        title = 'NTDS'
        format = 'ttf'
        data = [9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                104, 105, 116, 149, 156, 247, 249, 250]
        super().__init__(title, format, data)
