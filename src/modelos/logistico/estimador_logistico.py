import numpy as np


from src.modelos.estimador_modelo import EstimadorModelo


class EstimadorLogistico(EstimadorModelo):

    def calcular_media(self, t, *parametros_modelo):
        a, b, c = parametros_modelo
        return a / (1 + self.calcular_phi(b, c, t))

    def calcular_lambda(self, t, *parametros_modelo):
        a, b, c = parametros_modelo
        phi = self.calcular_phi(b, c, t)
        numerador = a * b * phi
        denominador = (1 + phi)**2
        return numerador/denominador

    def ecuaciones_mv_tiempo_hasta_la_falla(self, tiempos, n_fallas, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas),
                self.ecuacion_mv_2_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas),
                self.ecuacion_mv_3_tiempo_hasta_la_falla(a, b, c, tiempos, n_fallas))

    def ecuacion_mv_1_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_g = 0
        t = [0] + tiempos
        for k in range(len(t)):
            t_k = t[k]
            t_k_menos_1 = t[k - 1]
            suma_g += self.calcular_g(a, b, c, t_k, t_k_menos_1)

        return n_fallas - suma_g

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_h = 0
        t = [0] + tiempos
        for k in range(1, len(t)):
            t_k = t[k]
            t_k_menos_1 = t[k - 1]
            suma_h += self.calcular_h(a, b, c, t_k, t_k_menos_1)

        suma_tk = np.sum(tiempos)
        suma_cuarto_termino = 0
        for k in range(1, len(t)):
            t_k = t[k]
            psi_tk = self.calcular_psi(b, c, t_k)
            mu_tk = self.calcular_media(t_k, a, b, c)
            suma_cuarto_termino += (psi_tk * mu_tk)

        return n_fallas/b - suma_tk + n_fallas * c + (2/a) * suma_cuarto_termino - a * suma_h

    def ecuacion_mv_3_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_j = 0
        t = [0] + tiempos
        for k in range(1, len(t)):
            t_k = t[k]
            t_k_menos_1 = t[k - 1]
            suma_j += self.calcular_j(a, b, c, t_k, t_k_menos_1)

        suma_segundo_termino = 0
        for k in range(1, len(t)):
            t_k = t[k]
            phi_tk = self.calcular_phi(b, c, t_k)
            mu_tk = self.calcular_media(t_k, a, b, c)
            suma_segundo_termino += (phi_tk * mu_tk)

        return n_fallas - (2/a) * suma_segundo_termino - (1/a) * suma_j

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_3_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        pass

    def ecuacion_mv_2_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        pass

    def ecuacion_mv_3_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        pass

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_3_fallas_por_dia(a, b, c, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        fallas_acumuladas_al_dia = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma_yi = np.sum(fallas_acumuladas_al_dia)
        suma_segundo_termino = 0
        for i in range(len(dias)):
            t_i = dias[i]
            suma_segundo_termino += (1 / self.calcular_phi(b, c, t_i))

        return suma_yi/a - suma_segundo_termino

    def ecuacion_mv_2_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        fallas_acumuladas_al_dia = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            y_i = fallas_acumuladas_al_dia[i]
            phi_i = self.calcular_phi(b, c, t_i)
            primer_factor = (t_i - c)/(1 + phi_i)
            corchete = y_i + (a / (1 + phi_i))
            suma += primer_factor * corchete

        return suma

    def ecuacion_mv_3_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        fallas_acumuladas_al_dia = self.calcular_fallas_acumuladas(fallas_por_dia)
        suma = 0
        for i in range(len(dias)):
            t_i = dias[i]
            y_i = fallas_acumuladas_al_dia[i]
            phi_i = self.calcular_phi(b, c, t_i)
            primer_factor = b / (1 + phi_i)
            corchete = -y_i + (a / (1 + phi_i))
            suma += primer_factor * corchete

        return suma

    def calcular_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calcular_psi(self, b, c, t):
        return (t - c) * self.calcular_phi(b, c, t)

    def calcular_g(self, a, b, c, t_1, t_2):
        mu_t1 = self.calcular_media(t_1, a, b, c)
        mu_t2 = self.calcular_media(t_2, a, b, c)
        return mu_t1 - mu_t2

    def calcular_h(self, a, b, c, t_1, t_2):
        psi_t1 = self.calcular_psi(b, c, t_1)
        mu_t1 = self.calcular_media(t_1, a, b, c)
        psi_t2 = self.calcular_psi(b, c, t_2)
        mu_t2 = self.calcular_media(t_2, a, b, c)
        return psi_t1 * (mu_t1**2) - psi_t2 * (mu_t2**2)

    def calcular_j(self, a, b, c, t_1, t_2):
        phi_t1 = self.calcular_phi(b, c, t_1)
        mu_t1 = self.calcular_media(t_1, a, b, c)
        phi_t2 = self.calcular_phi(b, c, t_2)
        mu_t2 = self.calcular_media(t_2, a, b, c)
        return -phi_t1 * (mu_t1**2) + phi_t2 * (mu_t2**2)







