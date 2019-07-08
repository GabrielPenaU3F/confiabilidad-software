from src.dato import Dato
from src.tabla_de_datos_observados import TablaDeDatosObservados


class RepositorioDatos:

    datos =	{
      'ntds': [0, 9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
               104, 105, 116, 149, 156, 247, 249, 250],
      'agile_nro_1': [0, 36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                      232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                      419, 439]
    }

    '''
        Formatos permitidos:
        'ttf' (Time to failure) -> devuelve datos en forma de pares (numero de falla, tiempo de falla)
        'tbf' (Time between failures) -> devuelve datos en forma de pares (numero de falla, tiempo desde la ultima falla)
    '''
    @classmethod
    def proveer_datos_observados_proyecto_NTDS(cls, formato):

        datos_observados = []
        datos_ntds = cls.datos['ntds']

        if formato == 'ttf':
            for k in range(len(datos_ntds)):
                datos_observados.append(Dato(k, datos_ntds[k]))
            return TablaDeDatosObservados(datos_observados)

        elif formato == 'tbf':
            for k in range(1, len(datos_ntds)):
                datos_observados.append(Dato(k, datos_ntds[k] - datos_ntds[k-1]))
            return TablaDeDatosObservados(datos_observados)

    @classmethod
    def proveer_datos_observados_proyecto_agile_nro_1(cls, formato):

        datos_observados = []
        datos_agile_nro_1 = cls.datos['agile_nro_1']

        if formato == 'ttf':
            for k in range(len(datos_agile_nro_1)):
                datos_observados.append(Dato(k, datos_agile_nro_1[k]))
            return TablaDeDatosObservados(datos_observados)

        elif formato == 'tbf':
            for k in range(1, len(datos_agile_nro_1)):
                datos_observados.append(Dato(k, datos_agile_nro_1[k] - datos_agile_nro_1[k-1]))
            return TablaDeDatosObservados(datos_observados)

