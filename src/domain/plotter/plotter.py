from abc import ABC, abstractmethod

from src.data.data_repository import DataRepository
from src.domain.plotter.plot_strategy.barraza_contagion_plot_strategy import BarrazaContagionPlotStrategy
from src.domain.plotter.plot_strategy.ds_plot_strategy import DSPlotStrategy
from src.domain.plotter.plot_strategy.homogeneous_poisson_plot_strategy import HomogeneousPoissonPlotStrategy
from src.domain.plotter.plot_strategy.musa_okumoto_plot_strategy import MusaOkumotoPlotStrategy
from src.domain.plotter.plot_strategy.goel_okumoto_plot_strategy import GoelOkumotoPlotStrategy
from src.domain.plotter.plot_strategy.gompertz_plot_strategy import GompertzPlotStrategy
from src.domain.plotter.plot_strategy.logistic_plot_strategy import LogisticPlotStrategy
from matplotlib import pyplot as plt


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

    def plot_real_data(self, axes, x_data, cumulative_failures, project_title):
        axes.plot(x_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
                  label='Real data (' + project_title + ')')

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

    def do_format_mt_plot(self, axes):
        axes.set_xlabel('Failure')
        self.config_axes_limits(axes)
        self.config_plot_background(axes)
        axes.legend()
        plt.show()

    def obtain_full_data(self, project_name):
        data = DataRepository.provide_project_data(project_name)
        return data.get_project_title(), data.get_times(), data.get_cumulative_failures()

    def obtain_plot_data(self, times, cumulative_failures, optional_arguments):
        start = optional_arguments.get_initial_sample()
        end = optional_arguments.get_end_sample()
        return times[start:end], cumulative_failures[start:end]
