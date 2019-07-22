import numpy as np
import scipy.optimize as opt
from functools import partial
from scipy.optimize.nonlin import NoConvergence
from colorama import Fore, Back, Style

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorGoelOkumoto(EstimadorModelo):

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas, aprox_inicial):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas, aprox_inicial)
        return parametros

    def func_media(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (1 - self.calcular_phi(b, t))

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
        t_n = tiempos[-1]
        return a * (1 - self.calcular_phi(b, t_n)) - n_fallas

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos, n_fallas):
        t_n = tiempos[-1]
        suma_t = np.sum(tiempos)
        return suma_t + t_n * a * self.calcular_phi(b, t_n) - (n_fallas / b)

    def estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(self, dias, fallas_por_dia, aprox_inicial,
                                                                   metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_por_dia, dias, fallas_por_dia), aprox_inicial,
                            method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_por_dia))

    # Ecuaciones del paper
    
    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        suma_k = np.sum(fallas_por_dia)
        t_n = dias[-1]
        return suma_k - a * (1 - self.calcular_phi(b, t_n))

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        suma_phi = 0
        for i in range(len(dias)):
            t_k = dias[i]
            if i == 0:
                t_k_menos_1 = 0
            else:
                t_k_menos_1 = dias[i - 1]
            suma_phi += self.calcular_phi_paper(b, t_k_menos_1, t_k)
        return np.sum(fallas_por_dia) * suma_phi - dias[-1] * a * np.exp(-b * dias[-1])
        
    def calcular_phi_paper(self, b, t_k_menos_1, t_k):
        num = t_k_menos_1 * self.calcular_phi(b, t_k_menos_1) - t_k * self.calcular_phi(b, t_k)
        den = self.calcular_phi(b, t_k_menos_1) - self.calcular_phi(b, t_k)
        return num/den


    '''
    
    # Ecuaciones deducidas por mi
    
    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        n = len(fallas_por_dia)
        suma_k = np.sum(fallas_por_dia)
        suma_phi = 0
        for i in range(len(dias)):
            suma_phi += self.calcular_phi(b, dias[i])

        return suma_k/a - n + suma_phi

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        suma = 0
        for i in range(len(dias)):
            phi = self.calcular_phi(b, dias[i])
            primer_factor = dias[i] * phi
            factor_parentesis = (fallas_por_dia[i] / (1 - phi)) - a
            suma += primer_factor * factor_parentesis
        return suma
    '''

    def calcular_phi(self, b, t):
        return np.exp(-b * t)




