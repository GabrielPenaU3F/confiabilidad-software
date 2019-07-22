from abc import ABC, abstractmethod


class EstimadorModelo(ABC):

    @abstractmethod
    def func_media(self, t, *parametros_modelo):
        pass

    def calcular_prr(self, tiempos, fallas_acumuladas, *parametros_modelo):
        # El primer valor siempre es 0. Lo elimino para que pueda efectuarse la division
        tiempos = tiempos[1:]
        fallas_acumuladas = fallas_acumuladas[1:]

        fallas_estimadas = [self.func_media(tiempos[i], *parametros_modelo) for i in range(len(tiempos))]
        prr = 0
        for i in range(len(tiempos)):
            prr += (1 - fallas_acumuladas[i] / fallas_estimadas[i]) ** 2
        return prr

