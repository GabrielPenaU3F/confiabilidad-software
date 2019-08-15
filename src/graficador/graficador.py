from src.graficador.plot_strategy.ds_plot_strategy import DSPlotStrategy
from src.graficador.plot_strategy.goel_okumoto_plot_strategy import GoelOkumotoPlotStrategy
from src.graficador.plot_strategy.logistico_plot_strategy import LogisticoPlotStrategy


class Graficador:

    plot_strategy = {
        'goel-okumoto': GoelOkumotoPlotStrategy(),
        'delayed-s-shaped': DSPlotStrategy(),
        'logistico': LogisticoPlotStrategy()
    }

    def graficar(self, nombre_proyecto, modelo, params_mc, params_mv, datos):
        plot_strategy = self.get_estrategia_modelo(modelo)
        plot_strategy.graficar(nombre_proyecto, params_mc, params_mv, datos)

    def get_estrategia_modelo(self, modelo):
        return self.plot_strategy.get(modelo)
