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
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, tiempos, n_fallas),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, tiempos, n_fallas))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, tiempos, n_fallas):
        t_n = tiempos[-1]
        return self.calcular_media(t_n, a, b) - n_fallas

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, tiempos, n_datos):
        t_n = tiempos[-1]
        suma_tk = np.sum(tiempos)
        return suma_tk + a * t_n * self.calcular_exp_menos_bt(b, t_n) - (n_datos / b)

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        pass

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_acumuladas_al_dia):
        pass

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

    '''
    # Del paper

    def log_likelihood_ttf(self, tiempos, n_fallas, *parametros_modelo):
        a, b = parametros_modelo
        suma_ti = np.sum(tiempos)
        t_n = tiempos[-1]
        mu_tn = a * (1 - np.exp(-b * t_n))
        return n_fallas * np.log(a * b) - (b * suma_ti) - mu_tn

    # Del paper
    def log_likelihood_fpd(self, dias, fallas_por_dia, *parametros_modelo):
        a, b = parametros_modelo
        deltas = fallas_por_dia
        dias = [0] + dias
        t_n = dias[-1]
        suma_segundo_termino = 0
        for i in range(1, len(dias)):
            t_i_menos_1 = dias[i - 1]
            t_i = dias[i]
            delta_yi = deltas[i - 1]
            phi_t_i_menos_1 = self.calcular_exp_menos_bt(b, t_i_menos_1)
            phi_t_i = self.calcular_exp_menos_bt(b, t_i)
            primer_logaritmo = np.log(a * (phi_t_i_menos_1 - phi_t_i))
            # Aquí debe usarse np.math porque np.log no funciona con enteros tipo long
            segundo_logaritmo = np.math.log(np.math.factorial(delta_yi))
            suma_segundo_termino += delta_yi * (primer_logaritmo - segundo_logaritmo)
        return -a * self.calcular_exp_menos_bt(b, t_n) + suma_segundo_termino
        
    '''
    def calcular_exp_menos_bt(self, b, t):
        return np.exp(-b * t)







