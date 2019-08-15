from datos.repositorio_datos import RepositorioDatos
from src.excepciones.excepciones import FormatoNoAdmitidoException
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.modelos.goel_okumoto.estimador_goel_okumoto import EstimadorGoelOkumoto


class GoelOkumotoFitStrategy(FitStrategy):

    def fit_ttf(self, nombre_proyecto, datos):
        datos = RepositorioDatos.proveer_datos_observados_proyecto(nombre_proyecto)
        self.validar_formato(datos)
        ttf = datos.get_datos()
        fallas_acumuladas = datos.get_fallas_acumuladas()
        ttf_sin_cero = ttf[1:]

        go = EstimadorGoelOkumoto()
        aprox_inicial = (1, 0.5)
        params_go_mc = go.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas, aprox_inicial)

        params_go_mv = go.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf_sin_cero,
                                                                                            fallas_acumuladas,
                                                                                            params_go_mc,
                                                                                            metodo_resolucion='krylov')

        return params_go_mc, params_go_mv

    def fit_agrupados_acum(self, nombre_proyecto, datos):
        pass

    def fit_agrupados_fpd(self, nombre_proyecto, datos):
        pass

    def validar_formato(self, datos):
        if not datos.get_formato() == 'ttf':
            raise FormatoNoAdmitidoException('El proyecto seleccionado no admite el formato especificado')
