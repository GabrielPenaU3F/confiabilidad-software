from abc import ABC, abstractmethod
from functools import partial

import numpy as np
import scipy.optimize as opt
from colorama import Fore
from scipy.optimize.nonlin import NoConvergence


class EstimadorModelo(ABC):

    @abstractmethod
    def func_media(self, t, *parametros_modelo):
        pass

    def calcular_numero_medio_de_fallas(self, tiempos, *parametros_modelo):
        return self.func_media(np.array(tiempos), *parametros_modelo)

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas, aprox_inicial):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas, p0=aprox_inicial)
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

    def estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(self, dias, fallas_acumuladas_al_dia,
                                                                   aprox_inicial, metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_por_dia, dias, fallas_acumuladas_al_dia),
                            aprox_inicial, method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    @abstractmethod
    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_acumuladas_al_dia, vec):
        pass

    def calcular_prr(self, tiempos, fallas_acumuladas, *parametros_modelo):
        # El primer valor siempre es 0. Lo elimino para que pueda efectuarse la division
        tiempos = tiempos[1:]
        fallas_acumuladas = fallas_acumuladas[1:]

        fallas_estimadas = [self.func_media(tiempos[i], *parametros_modelo) for i in range(len(tiempos))]
        prr = 0
        for i in range(len(tiempos)):
            prr += (1 - fallas_acumuladas[i] / fallas_estimadas[i]) ** 2
        return prr

