from src.plotter.plot_strategy.barraza_contagion_plot_strategy import BarrazaContagionPlotStrategy
from src.plotter.plot_strategy.ds_plot_strategy import DSPlotStrategy
from src.plotter.plot_strategy.goel_okumoto_plot_strategy import GoelOkumotoPlotStrategy
from src.plotter.plot_strategy.gompertz_plot_strategy import GompertzPlotStrategy
from src.plotter.plot_strategy.logistic_plot_strategy import LogisticPlotStrategy


class Plotter:

    plot_strategy = {
        'goel-okumoto': GoelOkumotoPlotStrategy,
        'delayed-s-shaped': DSPlotStrategy,
        'logistic': LogisticPlotStrategy,
        'barraza-contagion': BarrazaContagionPlotStrategy,
        'gompertz': GompertzPlotStrategy
    }

    def plot(self, project_name, model, lsq_params, ml_params):
        plot_strategy = self.get_model_strategy(model)(project_name)
        plot_strategy.plot(project_name, lsq_params, ml_params)

    def get_model_strategy(self, model):
        return self.plot_strategy.get(model)
