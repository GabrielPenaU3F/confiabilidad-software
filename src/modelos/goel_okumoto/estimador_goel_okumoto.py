import numpy as np

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorGoelOkumoto(EstimadorModelo):

    def calcular_media(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (1 - self.calcular_exp_menos_bt(b, t))

    def calcular_lambda(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * b * self.calcular_exp_menos_bt(b, t)

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, n_fallas, vec):
        a, b = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos):
        n = len(tiempos)
        t_n = tiempos[-1]
        return self.calcular_media(t_n, a, b) - n

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos):
        n = len(tiempos)
        t_n = tiempos[-1]
        suma_tk = np.sum(tiempos)
        return suma_tk + a * t_n * self.calcular_exp_menos_bt(b, t_n) - (n/b)

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_acumuladas_al_dia(a, b, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        n = len(dias)
        suma_yi = np.sum(fallas_acumuladas_al_dia)
        suma_exp = 0
        for i in range(len(dias)):
            t_i = dias[i]
            suma_exp += self.calcular_exp_menos_bt(b, t_i)
        return (suma_yi / a) - n + suma_exp

    def ecuacion_mv_2_fallas_acumuladas_al_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        sumatoria = 0
        for i in range(len(dias)):
            t_i = dias[i]
            exp_b_ti = self.calcular_exp_menos_bt(b, t_i)
            parentesis = (fallas_acumuladas_al_dia[i] / (1 - exp_b_ti)) - a
            sumatoria += t_i * exp_b_ti * parentesis
        return sumatoria

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        suma_delta_yi = np.sum(deltas_yi)
        t_n = dias[-1]
        return suma_delta_yi - self.calcular_media(t_n, a, b)

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        t_n = dias[-1]
        deltas_yi = fallas_por_dia
        sumatoria_delta_por_phi = 0
        for i in range(len(dias)):
            t_i = dias[i]
            if i == 0:
                t_i_menos_1 = 0
            else:
                t_i_menos_1 = dias[i - 1]
            sumatoria_delta_por_phi += (deltas_yi[i] * self.calcular_phi(b, t_i, t_i_menos_1))
        return sumatoria_delta_por_phi + a * t_n * self.calcular_exp_menos_bt(b, t_n)

    def calcular_phi(self, b, t_i, t_i_menos_1):
        num = t_i_menos_1 * self.calcular_exp_menos_bt(b, t_i_menos_1) - t_i * self.calcular_exp_menos_bt(b, t_i)
        den = self.calcular_exp_menos_bt(b, t_i_menos_1) - self.calcular_exp_menos_bt(b, t_i)
        return num/den

    def calcular_exp_menos_bt(self, b, t):
        return np.exp(-b * t)







