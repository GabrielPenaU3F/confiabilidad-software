from datos.repositorio_datos import RepositorioDatos
from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.modelos.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped


class DSFitStrategy(FitStrategy):

    def fit_ttf(self, nombre_proyecto, datos):
        datos = RepositorioDatos.proveer_datos_observados_proyecto(nombre_proyecto)
        self.validar_formato(datos)
        ttf = datos.get_datos()
        fallas_acumuladas = datos.get_fallas_acumuladas()
        ttf_sin_cero = ttf[1:]

        ds = EstimadorDelayedSShaped()
        aprox_inicial = (1, 0.5)
        params_ds_mc = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas, aprox_inicial)

        params_ds_mv = ds.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf_sin_cero,
                                                                                            params_ds_mc,
                                                                                            metodo_resolucion='krylov')

        return params_ds_mc, params_ds_mv

    def fit_agrupados_acum(self, nombre_proyecto, datos):
        pass

    def fit_agrupados_fpd(self, nombre_proyecto, datos):
        pass

    def validar_formato(self, datos):
        pass

