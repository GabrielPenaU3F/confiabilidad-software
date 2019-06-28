import numpy as np
import scipy.optimize as opt
from functools import partial
from scipy.optimize.nonlin import NoConvergence
from colorama import Fore, Back, Style


class EstimadorDelayedSShaped:

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas)
        return parametros

    def func_media(self, x, a, b):
        return a * (1 - (1 + b*x) * np.exp(-b * x))

    def calcular_numero_medio_de_fallas(self, tiempos, a, b):
        return self.func_media(np.array(tiempos), a, b)

    # Los métodos 'hybr', 'lm' y 'krylov' son los únicos tres que funcionan para éste problema.
    # Para más detalles, consultar la documentación:
    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.root.html
    def estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(self, tiempos, aprox_inicial, metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_tiempo_hasta_la_falla, tiempos), aprox_inicial,
                            method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, vec):
        a, b = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos):
        suma = 0
        for r in range(len(tiempos)):
            suma += (r/a + (1 + b*tiempos[r])*np.exp(-b*tiempos[r]) - 1)
        return suma

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos):
        suma = 0
        for r in range(len(tiempos)):
            suma += ((tiempos[r]**2) * np.exp(-b*tiempos[r]) *
                     ((r / (1 - (1 + b*tiempos[r]) * np.exp(-b*tiempos[r]))) - a))
        return b * suma



