from datos.datos import DatosAgileN1, DatosNTDS, DatosMixedWaterfallAgile


class RepositorioDatos:

    datos = {
      'ntds': DatosNTDS(),
      'agile-n1': DatosAgileN1(),
      'mixed-waterfall-agile': DatosMixedWaterfallAgile()
    }

    @classmethod
    def proveer_datos_observados_proyecto(cls, nombre_proyecto):
        return cls.datos.get(nombre_proyecto)
