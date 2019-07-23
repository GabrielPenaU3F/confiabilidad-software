import numpy as np

from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorGoelOkumoto(EstimadorModelo):

    def func_media(self, t, *parametros_modelo):
        a, b = parametros_modelo
        return a * (1 - self.calcular_phi(b, t))

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

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, dias, fallas_por_dia))

    # Ecuaciones del paper

    '''
    
    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        delta_yi = fallas_por_dia
        suma_delta_yi = np.sum(delta_yi)
        t_n = dias[-1]
        return suma_delta_yi - a * (1 - self.calcular_phi(b, t_n))

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        t_n = dias[-1]
        suma_phi = 0
        for i in range(len(dias)):
            t_k = dias[i]
            if i == 0:
                t_k_menos_1 = 0
            else:
                t_k_menos_1 = dias[i - 1]
            suma_phi += self.calcular_phi_paper(b, t_k_menos_1, t_k)
        return -np.sum(fallas_por_dia) * suma_phi - t_n * a * self.calcular_phi(b, t_n)
    
    '''

    def calcular_phi_paper(self, b, t_k_menos_1, t_k):
        num = t_k_menos_1 * self.calcular_phi(b, t_k_menos_1) - t_k * self.calcular_phi(b, t_k)
        den = self.calcular_phi(b, t_k_menos_1) - self.calcular_phi(b, t_k)
        return num/den


    
    # Ecuaciones deducidas por mi
    
    def ecuacion_mv_1_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        n = len(fallas_por_dia)
        fallas_acumuladas = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma_ki = np.sum(fallas_acumuladas)
        suma_phi = 0
        for i in range(len(dias)):
            suma_phi += self.calcular_phi(b, dias[i])

        return suma_ki/a - n + suma_phi

    def ecuacion_mv_2_fallas_por_dia(self, a, b, dias, fallas_por_dia):
        suma = 0
        fallas_acumuladas = self.calcular_fallas_acumuladas(fallas_por_dia)
        for i in range(len(dias)):
            phi = self.calcular_phi(b, dias[i])
            primer_factor = dias[i] * phi
            factor_parentesis = (fallas_acumuladas[i] / (1 - phi)) - a
            suma += primer_factor * factor_parentesis
        return suma


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
            phi_t_i_menos_1 = self.calcular_phi(b, t_i_menos_1)
            phi_t_i = self.calcular_phi(b, t_i)
            primer_logaritmo = np.log(a * (phi_t_i_menos_1 - phi_t_i))
            # Aquí debe usarse np.math porque np.log no funciona con enteros tipo long
            segundo_logaritmo = np.math.log(np.math.factorial(delta_yi))
            suma_segundo_termino += delta_yi * (primer_logaritmo - segundo_logaritmo)
        return -a * self.calcular_phi(b, t_n) + suma_segundo_termino

    def calcular_phi(self, b, t):
        return np.exp(-b * t)






