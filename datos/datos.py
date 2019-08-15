from abc import ABC, abstractmethod

import numpy as np


class Datos(ABC):

    formato = None
    datos = None
    fallas_acumuladas = None

    def __init__(self, formato, datos):
        self.formato = formato
        self.datos = datos
        self.calcular_fallas_acumuladas(datos)

    @abstractmethod
    def calcular_fallas_acumuladas(self, datos):
        pass

    def get_fallas_acumuladas(self):
        return self.fallas_acumuladas

    def get_formato(self):
        return self.formato

    def get_datos(self):
        return self.datos


class DatosNTDS(Datos):

    def __init__(self):
        formato = 'ttf'
        datos = [0, 9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                 104, 105, 116, 149, 156, 247, 249, 250]
        super().__init__(formato, datos)

    def calcular_fallas_acumuladas(self, datos):
        return np.arange(0, len(datos), 1)


class DatosAgileN1(Datos):

    def __init__(self):
        formato = 'ttf'
        datos = [0, 36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                 232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                 419, 439]
        super().__init__(formato, datos)

    def calcular_fallas_acumuladas(self, datos):
        return np.arange(0, len(datos), 1)


class DatosMixedWaterfallAgile(Datos):

    def __init__(self):
        formato = 'agrupados'
        datos = [12, 22, 7, 3, 0, 1, 0, 0, 0, 3, 0, 0, 21, 5, 3, 1, 3, 0, 1, 2,
                 4, 1, 4, 1, 2, 4, 2, 2, 5, 3, 5, 2, 5, 2, 1, 7, 8, 3, 4, 27, 11, 12,
                 11, 8, 1, 3, 12, 1, 8, 6, 6, 3, 12, 17, 15, 18, 19, 16, 14, 8, 12,
                 11, 5, 6, 10, 1, 13, 10, 9, 7, 3, 7, 6, 6, 7, 9, 0, 8, 5, 8, 4, 2,
                 2, 2, 5, 3, 5, 1, 2, 0, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                 1, 3, 1, 3, 8, 2, 4, 7, 5, 3, 8, 7, 6, 2, 3, 6, 5, 5, 5, 1, 5, 1,
                 5, 3, 2, 5, 2, 5, 0, 3, 4, 2, 3, 1, 2, 1, 1, 0, 3, 1, 4, 3, 9, 1, 9,
                 1, 8, 6, 1, 4, 3, 5, 3, 0, 4, 5, 2, 0, 4, 1, 1, 1, 4, 6, 1, 5, 9,
                 1, 4, 5, 3, 3, 4, 5, 5, 2, 2, 3, 3, 5, 5, 5, 1, 3, 3, 0, 1, 3, 0, 1,
                 2, 2, 2, 1, 4, 2, 1, 0, 0, 2, 4, 2, 3, 1]
        super().__init__(formato, datos)

    def calcular_fallas_acumuladas(self, datos):
        return np.cumsum(datos)
