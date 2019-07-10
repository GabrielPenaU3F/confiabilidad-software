class TablaDeDatosFallaTiempo:

    def __init__(self, datos):
        fallas = []
        tiempos = []
        for dato in datos:
            fallas.append(dato.get_numero())
            tiempos.append(dato.get_tiempo())

        self.fallas = fallas
        self.tiempos_falla = tiempos

    def get_tiempos_de_falla(self):
        return self.tiempos_falla

    def get_fallas_acumuladas(self):
        return self.fallas

    def get_cantidad_datos(self):
        return self.fallas[-1]
