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
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        t_n = tiempos[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        return n_fallas - (mu_tn - mu_t0)

    def ecuacion_mv_2_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_tk = np.sum(tiempos)
        suma_cuarto_termino = 0
        for k in range(len(tiempos)):
            t_k = tiempos[k]
            psi_tk = self.calcular_psi(b, c, t_k)
            mu_tk = self.calcular_media(t_k, a, b, c)
            suma_cuarto_termino += (psi_tk * mu_tk)

        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        psi_t0 = self.calcular_psi(b, c, t_0)
        t_n = tiempos[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        psi_tn = self.calcular_psi(b, c, t_n)
        quinto_termino = (mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0

        return n_fallas/b + suma_tk - n_fallas * c + (2/a) * suma_cuarto_termino + (1/a) * quinto_termino

    def ecuacion_mv_3_tiempo_hasta_la_falla(self, a, b, c, tiempos, n_fallas):
        suma_segundo_termino = 0
        for k in range(len(tiempos)):
            t_k = tiempos[k]
            mu_tk = self.calcular_media(t_k, a, b, c)
            phi_tk = self.calcular_phi(t_k, b, c)
            suma_segundo_termino += mu_tk * phi_tk

        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        phi_t0 = self.calcular_phi(b, c, t_0)
        t_n = tiempos[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        phi_tn = self.calcular_phi(b, c, t_n)
        quinto_termino = (mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0

        return n_fallas * a - 2 * suma_segundo_termino - quinto_termino

    def ecuaciones_mv_fallas_acumuladas_al_dia(self, dias, fallas_acumuladas_al_dia, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_2_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia),
                self.ecuacion_mv_3_fallas_acumuladas_al_dia(a, b, c, dias, fallas_acumuladas_al_dia))

    def ecuacion_mv_1_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        sumatoria = 0
        for i in range(len(dias)):
            t_i = dias[i]
            y_i = fallas_acumuladas_al_dia[i]
            mu_ti = self.calcular_media(t_i, a, b, c)
            sumatoria += (y_i - mu_ti)

        n = len(dias)
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        return sumatoria + n * mu_t0

    def ecuacion_mv_2_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        n = len(dias)
        sumatoria = 0
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        psi_t0 = self.calcular_psi(b, c, t_0)
        for i in range(len(dias)):
            y_i = fallas_acumuladas_al_dia[i]
            t_i = dias[i]
            mu_ti = self.calcular_media(t_i, a, b, c)
            psi_ti = self.calcular_psi(b, c, t_i)
            numerador_primer_termino = psi_ti * (mu_ti**2) - psi_t0 * (mu_t0**2)
            denominador_primer_termino = psi_ti - psi_t0
            sumatoria += (y_i * numerador_primer_termino/denominador_primer_termino - psi_ti * (mu_ti**2))
        return sumatoria + n * psi_t0 * (mu_t0**2)

    def ecuacion_mv_3_fallas_acumuladas_al_dia(self, a, b, c, dias, fallas_acumuladas_al_dia):
        n = len(dias)
        sumatoria = 0
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        phi_t0 = self.calcular_phi(b, c, t_0)
        for i in range(len(dias)):
            y_i = fallas_acumuladas_al_dia[i]
            t_i = dias[i]
            mu_ti = self.calcular_media(t_i, a, b, c)
            phi_ti = self.calcular_phi(b, c, t_i)
            numerador_primer_termino = phi_ti * (mu_ti**2) - phi_t0 * (mu_t0**2)
            denominador_primer_termino = phi_ti - phi_t0
            sumatoria += (y_i * numerador_primer_termino/denominador_primer_termino - phi_ti * (mu_ti**2))
        return sumatoria + n * phi_t0 * (mu_t0**2)

    def ecuaciones_mv_fallas_por_dia(self, dias, fallas_por_dia, vec):
        a, b, c = vec
        return (self.ecuacion_mv_1_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_2_fallas_por_dia(a, b, c, dias, fallas_por_dia),
                self.ecuacion_mv_3_fallas_por_dia(a, b, c, dias, fallas_por_dia))

    def ecuacion_mv_1_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        suma_delta_yi = np.sum(deltas_yi)
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        t_n = dias[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        return suma_delta_yi - (mu_tn - mu_t0)

    def ecuacion_mv_2_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        psi_t0 = self.calcular_psi(b, c, t_0)
        t_n = dias[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        psi_tn = self.calcular_psi(b, c, t_n)
        sumatoria = 0
        for i in range(len(dias)):
            t_i = dias[i]
            if i == 0:
                t_i_menos_1 = t_0
            else:
                t_i_menos_1 = dias[i - 1]
            delta_yi = deltas_yi[i]
            mu_ti = self.calcular_media(t_i, a, b, c)
            psi_ti = self.calcular_psi(b, c, t_i)
            mu_ti_menos_1 = self.calcular_media(t_i_menos_1, a, b, c)
            psi_ti_menos_1 = self.calcular_psi(b, c, t_i_menos_1)
            numerador = (mu_ti**2) * psi_ti - (mu_ti_menos_1**2) * psi_ti_menos_1
            denominador = mu_ti - mu_ti_menos_1
            sumatoria += delta_yi * numerador / denominador
        return sumatoria - ((mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0)

    def ecuacion_mv_3_fallas_por_dia(self, a, b, c, dias, fallas_por_dia):
        deltas_yi = fallas_por_dia
        t_0 = 0
        mu_t0 = self.calcular_media(t_0, a, b, c)
        phi_t0 = self.calcular_phi(b, c, t_0)
        t_n = dias[-1]
        mu_tn = self.calcular_media(t_n, a, b, c)
        phi_tn = self.calcular_phi(b, c, t_n)
        sumatoria = 0
        for i in range(len(dias)):
            t_i = dias[i]
            if i == 0:
                t_i_menos_1 = t_0
            else:
                t_i_menos_1 = dias[i - 1]
            delta_yi = deltas_yi[i]
            mu_ti = self.calcular_media(t_i, a, b, c)
            phi_ti = self.calcular_phi(b, c, t_i)
            mu_ti_menos_1 = self.calcular_media(t_i_menos_1, a, b, c)
            phi_ti_menos_1 = self.calcular_phi(b, c, t_i_menos_1)
            numerador = -(mu_ti**2) * phi_ti + (mu_ti_menos_1**2) * phi_ti_menos_1
            denominador = mu_ti - mu_ti_menos_1
            sumatoria += delta_yi * numerador / denominador
        return sumatoria - ((mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0)

    def calcular_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calcular_psi(self, b, c, t):
        return (t - c) * self.calcular_phi(b, c, t)








