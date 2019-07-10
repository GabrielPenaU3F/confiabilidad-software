from src.dato_dia_fallas import DatoDiaFallas
from src.dato_falla_tiempo import DatoFallaTiempo
from src.tabla_de_datos_dia_fallas import TablaDeDatosDiaFallas
from src.tabla_de_datos_falla_tiempo import TablaDeDatosFallaTiempo


class RepositorioDatos:

    datos_ttf = {
      'ntds': [0, 9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
               104, 105, 116, 149, 156, 247, 249, 250],
      'agile_nro_1': [0, 36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                      232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                      419, 439]
    }

    datos_fpd = {
        'mixed_waterfall_agile': [12, 22, 7, 3, 0, 1, 0, 0, 0, 3, 0, 0, 21, 5, 3, 1, 3, 0, 1, 2,
                                  4, 1, 4, 1, 2, 4, 2, 2, 5, 3, 5, 2, 5, 2, 1, 7, 8, 3, 4, 27, 11, 12,
                                  11, 8, 1, 3, 12, 1, 8, 6, 6, 3, 12, 17, 15, 18, 19, 16, 14, 8, 12,
                                  11, 5, 6, 10, 1, 13, 10, 9, 7, 3, 7, 6, 6, 7, 9, 0, 8, 5, 8, 4, 2,
                                  2, 2, 5, 3, 5, 1, 2, 0, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                                  1, 3, 1, 3, 8, 2, 4, 7, 5, 3, 8, 7, 6, 2, 3, 6, 5, 5, 5, 1, 5, 1,
                                  5, 3, 2, 5, 2, 5, 0, 3, 4, 2, 3, 1, 2, 1, 1, 0, 3, 1, 4, 3, 9, 1, 9,
                                  1, 8, 6, 1, 4, 3, 5, 3, 0, 4, 5, 2, 0, 4, 1, 1, 1, 4, 6, 1, 5, 9,
                                  1, 4, 5, 3, 3, 4, 5, 5, 2, 2, 3, 3, 5, 5, 5, 1, 3, 3, 0, 1, 3, 0, 1,
                                  2, 2, 2, 1, 4, 2, 1, 0, 0, 2, 4, 2, 3, 1]
    }


    '''
        Formatos permitidos:
        
        Proyectos: NTDS % Agile nro 1
        'ttf' (Time to failure) -> devuelve datos en forma de pares (numero de falla, tiempo de falla)
        'tbf' (Time between failures) -> devuelve datos en forma de pares (numero de falla, tiempo desde la ultima falla)
        
        Proyectos: Mixed Waterfall-Agile
        'fpd' (Failures per day) -> devuelve datos en forma de pares (dia, cantidad de fallas)
        
    '''
    @classmethod
    def proveer_datos_observados_proyecto_NTDS(cls, formato):

        datos_observados = []
        datos_ntds = cls.datos_ttf['ntds']

        if formato == 'ttf':
            for k in range(len(datos_ntds)):
                datos_observados.append(DatoFallaTiempo(k, datos_ntds[k]))
            return TablaDeDatosFallaTiempo(datos_observados)

        elif formato == 'tbf':
            for k in range(1, len(datos_ntds)):
                datos_observados.append(DatoFallaTiempo(k, datos_ntds[k] - datos_ntds[k - 1]))
            return TablaDeDatosFallaTiempo(datos_observados)

    @classmethod
    def proveer_datos_observados_proyecto_agile_nro_1(cls, formato):

        datos_observados = []
        datos_agile_nro_1 = cls.datos_ttf['agile_nro_1']

        if formato == 'ttf':
            for k in range(len(datos_agile_nro_1)):
                datos_observados.append(DatoFallaTiempo(k, datos_agile_nro_1[k]))
            return TablaDeDatosFallaTiempo(datos_observados)

        elif formato == 'tbf':
            for k in range(1, len(datos_agile_nro_1)):
                datos_observados.append(DatoFallaTiempo(k, datos_agile_nro_1[k] - datos_agile_nro_1[k - 1]))
            return TablaDeDatosFallaTiempo(datos_observados)

    @classmethod
    def proveer_datos_observados_proyecto_mixed_waterfall_agile(cls, formato):

        datos_observados = []

        if formato == 'fpd':
            datos_mixed_waterfall_agile = cls.datos_fpd['mixed_waterfall_agile']
            for k in range(len(datos_mixed_waterfall_agile)):
                datos_observados.append(DatoDiaFallas(k + 1, datos_mixed_waterfall_agile[k]))
            return TablaDeDatosDiaFallas(datos_observados)

