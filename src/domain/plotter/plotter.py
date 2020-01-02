from abc import ABC, abstractmethod
from src.domain.plotter.plot_strategy.barraza_contagion_plot_strategy import BarrazaContagionPlotStrategy
from src.domain.plotter.plot_strategy.ds_plot_strategy import DSPlotStrategy
from src.domain.plotter.plot_strategy.homogeneous_poisson_plot_strategy import HomogeneousPoissonPlotStrategy
from src.domain.plotter.plot_strategy.musa_okumoto_plot_strategy import MusaOkumotoPlotStrategy
from src.domain.plotter.plot_strategy.goel_okumoto_plot_strategy import GoelOkumotoPlotStrategy
from src.domain.plotter.plot_strategy.gompertz_plot_strategy import GompertzPlotStrategy
from src.domain.plotter.plot_strategy.logistic_plot_strategy import LogisticPlotStrategy


class Plotter(ABC):

    plot_strategy = {
        'poisson': HomogeneousPoissonPlotStrategy,
        'musa-okumoto': MusaOkumotoPlotStrategy,
        'goel-okumoto': GoelOkumotoPlotStrategy,
        'delayed-s-shaped': DSPlotStrategy,
        'logistic': LogisticPlotStrategy,
        'barraza-contagion': BarrazaContagionPlotStrategy,
        'gompertz': GompertzPlotStrategy
    }

    @abstractmethod
    def plot_results(self, *args):
        pass

    @abstractmethod
    def plot_mttf(self, *args):
        pass

    @abstractmethod
    def plot_mtbf(self, *args):
        pass

    def get_model_strategy(self, model):
        return self.plot_strategy.get(model)

    def config_axes_limits(self, axes):
        axes.set_xlim(left=0, auto=True)
        axes.set_ylim(bottom=0, auto=True)

    def config_plot_background(self, axes):
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)
