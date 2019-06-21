import numpy as np
import scipy.optimize as opt


class EstimadorGoelOkumoto:

    def __init__(self):
        self.a = None
        self.b = None

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas)
        if self.a is None:
            self.a = parametros[0]
        if self.b is None:
            self.b = parametros[1]
        return parametros

    def func_media(self, x, a, b):
        return a * (1 - np.exp(-b * x))

    def calcular_numero_medio_de_fallas(self, tiempos):
        if self.a is not None and self.b is not None:
            return self.func_media(np.array(tiempos), self.a, self.b)

