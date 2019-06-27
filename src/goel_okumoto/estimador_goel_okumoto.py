import numpy as np
import scipy.optimize as opt
from functools import partial
from scipy.optimize.nonlin import NoConvergence
from colorama import Fore, Back, Style


class EstimadorGoelOkumoto:

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas)
        return parametros

    def func_media(self, x, a, b):
        return a * (1 - np.exp(-b * x))

    def calcular_numero_medio_de_fallas(self, tiempos, a, b):
            return self.func_media(np.array(tiempos), a, b)

    # Los métodos 'hybr', 'lm' y 'krylov' son los únicos tres que funcionan para éste problema.
    # Para más detalles, consultar la documentación:
    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.root.html
    def estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(self, tiempos, aprox_inicial):
        try:
            return opt.root(partial(self.ecuaciones_mv_tiempo_hasta_la_falla, tiempos), aprox_inicial,
                            method='krylov').x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, vec):
        a, b = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos):
        n_fallas = len(tiempos)
        t_ultima_falla = tiempos[-1]
        return a * (1 - np.exp(-b * t_ultima_falla)) - n_fallas

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos):
        n_fallas = len(tiempos)
        t_ultima_falla = tiempos[-1]
        suma_tiempos_falla = np.sum(tiempos)
        return suma_tiempos_falla + t_ultima_falla * a * np.exp(-b * t_ultima_falla) - (n_fallas / b)

    def estimar_parametros_por_maxima_verosimilitud_datos_agrupados(self, tiempos, fallas_acumuladas):
        try:
            return opt.broyden1(partial(self.ecuaciones_mv_datos_agrupados, tiempos, fallas_acumuladas), [1, 1])
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_datos_agrupados(self, tiempos, fallas_acumuladas, vec):
        a, b = vec
        return (self.ecuacion_mv_1_datos_agrupados(a, b, tiempos, fallas_acumuladas),
                self.ecuacion_mv_2_datos_agrupados(a, b, tiempos, fallas_acumuladas))

    # Corregir
    def ecuacion_mv_1_datos_agrupados(self, a, b, tiempos, fallas_acumuladas):
        return fallas_acumuladas[-1] - a * (1 - np.exp(-b * tiempos[-1]))

    # Corregir
    def ecuacion_mv_2_datos_agrupados(self, a, b, tiempos, fallas_acumuladas):
        suma_phi = 0
        for i in range(len(tiempos)):
            if i == 0:
                suma_phi += self.calcular_phi(b, 0, tiempos[i])
            else:
                suma_phi += self.calcular_phi(b, tiempos[i - 1], tiempos[i])
        return -fallas_acumuladas[-1] * suma_phi - tiempos[-1] * a * np.exp(-b * tiempos[-1])

    def calcular_phi(self, b, t_k_menos_1, t_k):
        num = t_k_menos_1 * np.exp(-b * t_k_menos_1) - t_k * np.exp(-b * t_k)
        den = np.exp(-b * t_k_menos_1) - np.exp(-b * t_k)
        return num/den

