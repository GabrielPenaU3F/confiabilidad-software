from datos.repositorio_datos import RepositorioDatos
from src.excepciones.excepciones import FormatoNoAdmitidoException
from src.fitters.fit_strategy.fit_strategy import FitStrategy


class GoelOkumotoStrategy(FitStrategy):

    def fit_ttf(self, nombre_proyecto, datos):
        datos = RepositorioDatos.proveer_datos_observados_proyecto(nombre_proyecto)
        self.validar_formato(datos)
        ttf = datos.get_datos()
        fallas_acumuladas = datos.calcular_fallas_acumuladas()
        n_fallas = fallas_acumuladas[-1]
        ttf_sin_cero = ttf[1:]

    def fit_agrupados_acum(self, nombre_proyecto, datos):
        pass

    def fit_agrupados_fpd(self, nombre_proyecto, datos):
        pass

    def validar_formato(self, datos):
        if not datos.get_formato().equal('ttf'):
            raise FormatoNoAdmitidoException('El proyecto seleccionado no admite el formato especificado')
