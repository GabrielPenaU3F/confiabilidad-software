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
        t_n = tiempos[-1]
        return n_fallas - self.calcular_media(t_n, a, b, c)

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_tk = np.sum(tiempos)
        suma_cuarto_termino = 0
        for k in range(len(tiempos)):
            t_k = tiempos[k]
            psi_tk = self.calcular_psi(b, c, t_k)
            mu_tk = self.calcular_media(t_k, a, b, c)
            suma_cuarto_termino += (psi_tk * mu_tk)

        t_n = tiempos[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        psi_tn = self.calcular_psi(b, c, t_n)
        return n_fallas/b - suma_tk + n_fallas * c + (2/a) * suma_cuarto_termino - (1/a) * psi_tn * (mu_tn**2)

    def ecuacion_mv_3_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_mu_tk = 0
        for k in range(len(tiempos)):
            t_k = tiempos[k]
            mu_tk = self.calcular_media(t_k, a, b, c)
            suma_mu_tk += mu_tk

        t_n = tiempos[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        phi_tn = self.calcular_phi(b, c, t_n)
        return n_fallas - (2/a) * suma_mu_tk - (1/a) * phi_tn * (mu_tn**2)

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
            suma += (primer_factor * corchete)
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
            suma += (primer_factor * corchete)
        return suma

    def calcular_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calcular_psi(self, b, c, t):
        return (t - c) * self.calcular_phi(b, c, t)








