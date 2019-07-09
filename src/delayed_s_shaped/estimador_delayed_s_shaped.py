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
    def estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(self, tiempos, n_fallas, aprox_inicial,
                                                                          metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_tiempo_hasta_la_falla, tiempos, n_fallas), aprox_inicial,
                            method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, n_fallas, vec):
        a, b = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos, n_fallas),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos, n_fallas))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos, n_fallas):
        return n_fallas/a + (1 + b * tiempos[-1]) * np.exp(-b * tiempos[-1]) - 1

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos, n_fallas):
        suma_ti = np.sum(tiempos)
        return (2 * n_fallas / b) - suma_ti - a * b * (tiempos[-1]**2) * np.exp(-b * tiempos[-1])



