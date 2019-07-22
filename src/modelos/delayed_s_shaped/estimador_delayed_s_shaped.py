import numpy as np

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorDelayedSShaped(EstimadorModelo):

    def func_media(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (1 - (1 + b*t) * np.exp(-b * t))

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

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        fallas_acumuladas_al_dia = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma_ki = np.sum(fallas_acumuladas_al_dia)
        segundo_termino = 0
        for i in range(len(dias)):
            t_i = dias[i]
            segundo_termino += (1 - (1 + b * t_i) * np.exp(-b * t_i))
        return suma_ki/a - segundo_termino

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        fallas_acumuladas_al_dia = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            k_i = fallas_acumuladas_al_dia[i]
            corchete = (k_i / (1 - (1 + b * t_i) * np.exp(-b * t_i)) - a)
            suma += (t_i ** 2) * np.exp(-b * t_i) * corchete
        return b * suma

    def log_likelihood_ttf(self, tiempos, n_fallas, *parametros_modelo):
        pass

    def log_likelihood_fpd(self, dias, fallas_por_dia, *parametros_modelo):
        pass

