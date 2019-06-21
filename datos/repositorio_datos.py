from src.dato import Dato
from src.tabla_de_datos_observados import TablaDeDatosObservados


class RepositorioDatos:

    datos_ntds = [9, 21, 32, 36, 43, 45, 50, 58, 63, 70, 71, 77, 78, 87, 91, 92, 95, 98,
                  104, 105, 116, 149, 156, 247, 249, 250]

    # Formato de datos: numero de falla - tiempo de falla
    @classmethod
    def proveer_datos_observados_proyecto_NTDS(cls):

        datos_observados = []
        for k in range(len(cls.datos_ntds)):
            datos_observados.append(Dato(k, cls.datos_ntds[k]))

        return TablaDeDatosObservados(datos_observados)

