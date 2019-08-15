from datos.repositorio_datos import RepositorioDatos
from src.fitters.fitter import Fitter
from src.graficador.graficador import Graficador


class TTFFitter(Fitter):

    """
    Modelos aceptados
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logístico: 'logistico'
    """
    def fit(self, modelo, nombre_proyecto):
        datos = RepositorioDatos.proveer_datos_observados_proyecto(nombre_proyecto)
        fit_strategy = self.get_estrategia_modelo(modelo)
        params_mc, params_mv = fit_strategy.fit_ttf(nombre_proyecto, datos)

        plotter = Graficador()
        plotter.graficar(nombre_proyecto, modelo, params_mc, params_mv, datos)

