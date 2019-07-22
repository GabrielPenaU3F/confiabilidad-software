import numpy as np
import scipy.optimize as opt
from functools import partial
from scipy.optimize.nonlin import NoConvergence
from colorama import Fore, Back, Style

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorLogistico(EstimadorModelo):

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas, aprox_inicial):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas, aprox_inicial)
        return parametros

    def func_media(self, t, *parametros_modelo):
        a, b, c = parametros_modelo
        return a / (1 + np.exp(-b * (t - c)))

    def calcular_numero_medio_de_fallas(self, tiempos, a, b, c):
        return self.func_media(np.array(tiempos), a, b, c)

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
        a, b, c = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas),
                self.ecuacion_mv_3_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_g = 0
        t = [0] + tiempos
        for i in range(1, len(t)):
            t_k = t[i]
            t_k_menos_1 = t[i - 1]
            suma_g += self.calcular_g(b, c, t_k, t_k_menos_1)

        return n_fallas/a - suma_g

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_h = 0
        t = [0] + tiempos
        for i in range(1, len(t)):
            t_k = t[i]
            t_k_menos_1 = t[i - 1]
            suma_h += self.calcular_h(b, c, t_k, t_k_menos_1)

        suma_tk = np.sum(tiempos)
        suma_cuarto_termino = 0
        for i in range(1, len(t)):
            t_k = t[i]
            phi_t_k = self.calcular_phi(b, c, t_k)
            suma_cuarto_termino += ((t_k - c) * phi_t_k) / (1 + phi_t_k)

        return n_fallas/b - suma_tk + n_fallas*c + 2*suma_cuarto_termino - a*suma_h

    def ecuacion_mv_3_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_j = 0
        t = [0] + tiempos
        for i in range(1, len(t)):
            t_k = t[i]
            t_k_menos_1 = t[i - 1]
            suma_j += self.calcular_j(b, c, t_k, t_k_menos_1)

        suma_segundo_termino = 0
        for i in range(1, len(t)):
            t_k = t[i]
            phi_t_k = self.calcular_phi(b, c, t_k)
            suma_segundo_termino += (b * phi_t_k) / (1 + phi_t_k)

        return n_fallas*b - 2*suma_segundo_termino - a*suma_j

    # phi(b, c, t) = e^{-b(t - c)}
    def calcular_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calcular_g(self, b, c, t_k, t_k_menos_1):
        primer_termino = 1/(1 + self.calcular_phi(b, c, t_k))
        segundo_termino = 1/(1 + self.calcular_phi(b, c, t_k_menos_1))
        return primer_termino - segundo_termino

    def calcular_h(self, b, c, t_k, t_k_menos_1):
        phi_t_k = self.calcular_phi(b, c, t_k)
        phi_t_k_menos_1 = self.calcular_phi(b, c, t_k_menos_1)
        primer_termino = ((t_k - c) * phi_t_k) / ((1 + phi_t_k)**2)
        segundo_termino = ((t_k_menos_1 - c) * phi_t_k_menos_1) / ((1 + phi_t_k_menos_1)**2)
        return primer_termino - segundo_termino

    def calcular_j(self, b, c, t_k, t_k_menos_1):
        phi_t_k = self.calcular_phi(b, c, t_k)
        phi_t_k_menos_1 = self.calcular_phi(b, c, t_k_menos_1)
        primer_termino = b * phi_t_k / ((1 + phi_t_k)**2)
        segundo_termino = b * phi_t_k_menos_1 / ((1 + phi_t_k_menos_1)**2)
        return - primer_termino + segundo_termino

    def estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(self, dias, fallas_por_dia, aprox_inicial,
                                                                   metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_por_dia, dias, fallas_por_dia), aprox_inicial,
                            method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_3_fallas_por_dia(a, b, c, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        suma_ki = np.sum(fallas_por_dia)
        suma_segundo_termino = 0
        for i in range(len(dias)):
            t_i = dias[i]
            suma_segundo_termino += (1 / self.calcular_phi(b, c, t_i))

        return suma_ki/a - suma_segundo_termino

    def ecuacion_mv_2_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            k_i = fallas_por_dia[i]
            phi_i = self.calcular_phi(b, c, t_i)
            primer_factor = (t_i - c)/(1 + phi_i)
            corchete = k_i + (a / (1 + phi_i))
            suma += primer_factor * corchete

        return suma

    def ecuacion_mv_3_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            k_i = fallas_por_dia[i]
            phi_i = self.calcular_phi(b, c, t_i)
            primer_factor = b / (1 + phi_i)
            corchete = -k_i + (a / (1 + phi_i))
            suma += primer_factor * corchete

        return suma






