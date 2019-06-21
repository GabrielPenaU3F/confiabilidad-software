import numpy as np
import scipy.optimize as opt


class EstimadorGoelOkumoto:

    def __init__(self):
        pass

    def ajustar_numero_medio_de_fallas_por_minimos_cuadraods(self, tiempo, fallas_acumuladas):
        parametros, cov = opt.curve_fit(self.func_media, tiempo, fallas_acumuladas)
        return parametros

    def func_media(self, x, a, b):
        return a * (1 - np.exp(-b * x))

