from datos.datos import DatosAgileN1, DatosNTDS, DatosMixedWaterfallAgile


class RepositorioDatos:

    datos = {
      'ntds': DatosNTDS(),
      'agile_nro_1': DatosAgileN1(),
      'mixed_waterfall_agile': DatosMixedWaterfallAgile()
    }

    @classmethod
    def proveer_datos_observados_proyecto(cls, nombre_proyecto):
        return cls.datos.get(nombre_proyecto)
