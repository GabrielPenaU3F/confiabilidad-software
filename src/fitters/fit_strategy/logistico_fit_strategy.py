from datos.repositorio_datos import RepositorioDatos
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.modelos.logistico.estimador_logistico import EstimadorLogistico


class LogisticoFitStrategy(FitStrategy):

    def fit_ttf(self, nombre_proyecto, datos):
        datos = RepositorioDatos.proveer_datos_observados_proyecto(nombre_proyecto)
        self.validar_formato(datos)
        ttf = datos.get_datos()
        fallas_acumuladas = datos.get_fallas_acumuladas()
        ttf_sin_cero = ttf[1:]

        log = EstimadorLogistico()
        aprox_inicial = (10, 0.05, 20)
        params_log_mc = log.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas, aprox_inicial)

        params_log_mv = log.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf_sin_cero,
                                                                                              params_log_mc,
                                                                                              metodo_resolucion='krylov')

        return params_log_mc, params_log_mv

    def fit_agrupados_acum(self, nombre_proyecto, datos):
        pass

    def fit_agrupados_fpd(self, nombre_proyecto, datos):
        pass

    def validar_formato(self, datos):
        pass
