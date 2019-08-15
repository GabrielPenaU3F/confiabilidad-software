import numpy as np

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorDelayedSShaped(EstimadorModelo):

    def calcular_media(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (1 - (1 + b*t) * self.calcular_exp_menos_bt(b, t))

    def calcular_lambda(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (b**2) * t * self.calcular_exp_menos_bt(b, t)

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, vec):
        a, b = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos):
        n = len(tiempos)
        t_n = tiempos[-1]
        return n/a + (1 + b * t_n) * self.calcular_exp_menos_bt(b, t_n) - 1

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos):
        n = len(tiempos)
        suma_t_k = np.sum(tiempos)
        t_n = tiempos[-1]
        return (2 * n/b) - suma_t_k - a * b * (t_n**2) * self.calcular_exp_menos_bt(b, t_n)

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        suma_yi = np.sum(fallas_acumuladas_al_dia)
        suma_mu_ti = 0
        for i in range(len(dias)):
            t_i = dias[i]
            mu_ti = self.calcular_media(t_i, a, b)
            suma_mu_ti += mu_ti
        return suma_yi - suma_mu_ti

    def ecuacion_mv_2_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        sumatoria = 0
        for i in range(len(dias)):
            t_i = dias[i]
            y_i = fallas_acumuladas_al_dia[i]
            mu_ti = self.calcular_media(t_i, a, b)
            corchete = (y_i / mu_ti) - 1
            sumatoria += ((t_i**2) * self.calcular_exp_menos_bt(b, t_i) * corchete)
        return sumatoria

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        suma_delta_yi = np.sum(deltas_yi)
        t_n = dias[-1]
        mu_tn = self.calcular_media(t_n, a, b)
        return suma_delta_yi - mu_tn

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        sumatoria = 0
        for i in range (len(dias)):
            t_i = dias[i]
            if i == 0:
                t_i_menos_1 = 0
            else:
                t_i_menos_1 = dias[i - 1]
            delta_yi = deltas_yi[i]
            sumatoria += delta_yi * self.calcular_psi(b, t_i, t_i_menos_1) / self.calcular_phi(b, t_i, t_i_menos_1)
        t_n = dias[-1]
        return b * sumatoria - a * (1 + b * (t_n**2) * self.calcular_exp_menos_bt(b, t_n))

    def calcular_exp_menos_bt(self, b, t):
        return np.exp(-b * t)

    def calcular_phi(self, b, t_1, t_2):
        primer_termino = (1 + b*t_2) * self.calcular_exp_menos_bt(b, t_2)
        segundo_termino = (1 + b*t_1) * self.calcular_exp_menos_bt(b, t_1)
        return primer_termino - segundo_termino

    def calcular_psi(self, b, t_1, t_2):
        primer_termino = (t_1**2) * self.calcular_exp_menos_bt(b, t_1)
        segundo_termino = (t_2**2) * self.calcular_exp_menos_bt(b, t_2)
        return primer_termino - segundo_termino

