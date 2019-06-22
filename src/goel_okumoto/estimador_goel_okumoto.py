import numpy as np
import scipy.optimize as opt


class EstimadorGoelOkumoto:

    def ajustar_numero_medio_de_fallas_por_minimos_cuadrados(self, tiempos, fallas_acumuladas):
        parametros, cov = opt.curve_fit(self.func_media, tiempos, fallas_acumuladas)
        return parametros

    def func_media(self, x, a, b):
        return a * (1 - np.exp(-b * x))

    def calcular_numero_medio_de_fallas(self, tiempos, a, b):
            return self.func_media(np.array(tiempos), a, b)

    def estimar_parametros_por_maxima_verosimilitud(self, tiempos, fallas_acumuladas):
        return opt.fsolve(self.ecuaciones_mv, (1, 1), args=(tiempos, fallas_acumuladas))

    def ecuaciones_mv(self, vec, tiempos, fallas_acumuladas):
        a, b = vec
        return (self.ecuacion_mv_1(a, b, tiempos, fallas_acumuladas),
                self.ecuacion_mv_2(a, b, tiempos, fallas_acumuladas))

    def ecuacion_mv_1(self, a, b, tiempos, fallas_acumuladas):
        return fallas_acumuladas[-1] - a * (1 - np.exp(-b * tiempos[-1]))

    def ecuacion_mv_2(self, a, b, tiempos, fallas_acumuladas):
        suma_phi = 0
        for i in range(len(tiempos)):
            if i == 0:
                suma_phi += self.calcular_phi(b, 0, tiempos[i])
            else:
                suma_phi += self.calcular_phi(b, tiempos[i - 1], tiempos[i])
        return -fallas_acumuladas[-1] * suma_phi - tiempos[-1] * a * np.exp(-b * tiempos[-1])

    def calcular_phi(self, b, t_k_menos_1, t_k):
        num = t_k_menos_1 * np.exp(-b * t_k_menos_1) - t_k * np.exp(-b * t_k)
        den = np.exp(-b * t_k_menos_1) - np.exp(-b * t_k)
        return num/den

