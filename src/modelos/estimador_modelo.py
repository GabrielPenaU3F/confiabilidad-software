from abc import ABC, abstractmethod
from functools import partial

import numpy as np
import scipy.optimize as opt
from colorama import Fore
from scipy.optimize.nonlin import NoConvergence


class EstimadorModelo(ABC):

    @abstractmethod
    def calcular_media(self, t, *parametros_modelo):
        pass

    @abstractmethod
    def calcular_lambda(self, t, *parametros_modelo):
        pass

    def calcular_numero_medio_de_fallas(self, tiempos, *parametros_modelo):
        return self.calcular_media(np.array(tiempos), *parametros_modelo)

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas, aprox_inicial):
        parametros, cov = opt.curve_fit(self.calcular_media, tiempos, fallas_acumuladas, p0=aprox_inicial)
        return parametros

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

    @abstractmethod
    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, n_fallas, vec):
        pass

    def estimar_parametros_por_maxima_verosimilitud_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia,
                                                                             aprox_inicial, metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_acumuladas_al_dia, dias, fallas_acumuladas_al_dia),
                            aprox_inicial, method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    @abstractmethod
    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        pass

    def estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(self, tiempos, fallas_por_dia, aprox_inicial,
                                                                   metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_por_dia, tiempos, fallas_por_dia), aprox_inicial,
                            method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    @abstractmethod
    def ecuaciones_mv_fallas_por_dia(self, tiempos, fallas_por_dia, vec):
        pass

    def calcular_fallas_acumuladas(self, fallas_por_dia):
        fallas_acumuladas = [fallas_por_dia[0]]
        for i in range(1, len(fallas_por_dia)):
            fallas_acumuladas.append(fallas_por_dia[i] + fallas_acumuladas[i - 1])
        return fallas_acumuladas

    def calcular_prr(self, tiempos, fallas_acumuladas, *parametros_modelo):
        # El primer valor siempre es 0. Lo elimino para que pueda efectuarse la division
        tiempos = tiempos[1:]
        fallas_acumuladas = fallas_acumuladas[1:]

        fallas_estimadas = [self.calcular_media(tiempos[i], *parametros_modelo) for i in range(len(tiempos))]
        prr = 0
        for i in range(len(tiempos)):
            prr += (1 - fallas_acumuladas[i] / fallas_estimadas[i]) ** 2
        return prr

    def calcular_aic_tiempo_hasta_la_falla(self, tiempos, n_fallas, *parametros_modelo):
        return -2 * self.log_likelihood_ttf(tiempos, n_fallas, *parametros_modelo) + (2 * len(parametros_modelo))

    def calcular_aic_fallas_por_dia(self, dias, fallas_por_dia, *parametros_modelo):
        return -2 * self.log_likelihood_fpd(dias, fallas_por_dia, *parametros_modelo) + (2 * len(parametros_modelo))

    def calcular_aic_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas, *parametros_modelo):
        return -2 * self.log_likelihood_facum(dias, fallas_acumuladas, *parametros_modelo) + (2 * len(parametros_modelo))

    def log_likelihood_ttf(self, tiempos, n_fallas, *parametros_modelo):
        return 0

    def log_likelihood_fpd(self, dias, fallas_por_dia, *parametros_modelo):
        return 0

    def log_likelihood_facum(self, dias, fallas_acumuladas, *parametros_modelo):
        return 0
