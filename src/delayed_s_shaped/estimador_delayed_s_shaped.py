import numpy as np
import scipy.optimize as opt
from functools import partial
from scipy.optimize.nonlin import NoConvergence
from colorama import Fore, Back, Style


class EstimadorDelayedSShaped:

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas, aprox_inicial):
        # Probar con condiciones iniciales a=0, b=2. Resultado: a=61.3964 y b=0.003714
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas, p0=aprox_inicial)
        return parametros

    def func_media(self, t, a, b):
        return a * (1 - (1 + b*t) * np.exp(-b * t))

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
        return n_fallas/a + (1 + b * t_n) * np.exp(-b * t_n) - 1

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos, n_fallas):
        suma_t_k = np.sum(tiempos)
        t_n = tiempos[-1]
        return (2 * n_fallas / b) - suma_t_k - a * b * (t_n**2) * np.exp(-b * t_n)

    def estimar_parametros_por_maxima_verosimilitud_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia,
                                                                             aprox_inicial, metodo_resolucion):
        try:
            return opt.root(partial(self.ecuaciones_mv_fallas_acumuladas_al_dia, dias, fallas_acumuladas_al_dia),
                            aprox_inicial, method=metodo_resolucion).x
        except NoConvergence:
            print(Fore.RED + 'El sistema es incompatible')
            return None

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        suma_k = np.sum(fallas_acumuladas_al_dia)
        segundo_termino = 0
        for i in range(len(dias)):
            t_i = dias[i]
            segundo_termino += (1 - (1 + b * t_i) * np.exp(-b * t_i))
        return suma_k/a - segundo_termino

    def ecuacion_mv_2_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            k_i = fallas_acumuladas_al_dia[i]
            corchete = (k_i / (1 - (1 + b * t_i) * np.exp(-b * t_i)) - a)
            suma += (t_i ** 2) * np.exp(-b * t_i) * corchete
        return b * suma 


