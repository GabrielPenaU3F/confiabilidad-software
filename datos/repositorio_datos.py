from src.dato import Dato
from src.tabla_de_datos_observados import TablaDeDatosObservados


class RepositorioDatos:

    # La tabla que figura en el paper no tiene el 0 al principio, yo entiendo que eso es un error
    # Si bien se vé que en el paper lo hicieron así, para mí está mal porque la curva arranca en 9,
    # como si hubiera 0 fallas al día 9. No tiene sentido por como presentan los datos.
    # Además, poniendo el 0 al inicio el modelo DS ajusta excelente, sino no anda.
    datos_ntds = [0, 9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                  104, 105, 116, 149, 156, 247, 249, 250]

    datos_proyecto_agile_nro_1 = [0, 36, 104, 118, 135, 142, 146, 147, 215, 217, 224, 231, 231, 231,
                        232, 236, 244, 314, 314, 314, 324, 324, 363, 376, 383, 386, 391, 414,
                        419, 439]

    # Formato de datos: numero de falla - tiempo de falla
    @classmethod
    def proveer_datos_observados_proyecto_NTDS(cls):

        datos_observados = []
        for k in range(len(cls.datos_ntds)):
            datos_observados.append(Dato(k, cls.datos_ntds[k]))

        return TablaDeDatosObservados(datos_observados)

    @classmethod
    def proveer_datos_observados_proyecto_agile_nro_1(cls):

        datos_observados = []
        for k in range(len(cls.datos_proyecto_agile_nro_1)):
            datos_observados.append(Dato(k, cls.datos_proyecto_agile_nro_1[k]))

        return TablaDeDatosObservados(datos_observados)

