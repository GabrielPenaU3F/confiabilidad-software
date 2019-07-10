import numpy as np

class TablaDeDatosDiaFallas:

    def __init__(self, datos):
        dias = []
        fallas_por_dia = []
        for dato in datos:
            dias.append(dato.get_dia())
            fallas_por_dia.append(dato.get_cantidad_de_fallas())

        self.dias = dias
        self.fallas_por_dia = fallas_por_dia

    def get_dias(self):
        return self.dias

    def get_fallas_por_dia(self):
        return self.fallas_por_dia

    def get_fallas_acumuladas(self):
        fallas_acumuladas = []
        for i in range(len(self.dias)):
            fallas_acumuladas.append(np.sum(self.fallas_por_dia[0:i+1]))

        return fallas_acumuladas

    def get_cantidad_datos(self):
        return self.dias[-1]
