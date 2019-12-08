import numpy as np

from src.plotter.plot_strategy.barraza_contagion_plot_strategy import BarrazaContagionPlotStrategy
from src.plotter.plot_strategy.ds_plot_strategy import DSPlotStrategy
from src.plotter.plot_strategy.musa_okumoto_plot_strategy import MusaOkumotoPlotStrategy
from src.plotter.plot_strategy.goel_okumoto_plot_strategy import GoelOkumotoPlotStrategy
from src.plotter.plot_strategy.gompertz_plot_strategy import GompertzPlotStrategy
from src.plotter.plot_strategy.logistic_plot_strategy import LogisticPlotStrategy
from matplotlib import pyplot as plt


class Plotter:

    plot_strategy = {
        'musa-okumoto': MusaOkumotoPlotStrategy,
        'goel-okumoto': GoelOkumotoPlotStrategy,
        'delayed-s-shaped': DSPlotStrategy,
        'logistic': LogisticPlotStrategy,
        'barraza-contagion': BarrazaContagionPlotStrategy,
        'gompertz': GompertzPlotStrategy
    }

    def plot_results(self, project_name, model, lsq_params, ml_params):
        plot_strategy = self.get_model_strategy(model)(project_name)
        plot_strategy.plot(project_name, lsq_params, ml_params)
        plt.show()

    def plot_mttf(self, mttf):
        fig, axes = plt.subplots()
        failures = np.linspace(1, len(mttf), len(mttf))
        if len(failures) >= 100:
            failures = failures[0:100]
            mttf = mttf[0:100]
        axes.set_ylabel('MTTF')
        markerline, stemlines, baseline = axes.stem(
            failures, mttf, basefmt='black', linefmt='#ca3e47', label='MTTF', use_line_collection=True)
        self.do_format_mt_plot(axes, markerline)

    def plot_mtbf(self, mtbf):
        fig, axes = plt.subplots()
        failures = np.linspace(1, len(mtbf), len(mtbf))
        if len(failures) >= 100:
            failures = failures[0:100]
            mtbf = mtbf[0:100]
        axes.set_ylabel('MTBF')
        markerline, stemlines, baseline = axes.stem(
            failures, mtbf, basefmt='black', linefmt='#ca3e47', label='MTBF', use_line_collection=True)
        self.do_format_mt_plot(axes, markerline)

    def do_format_mt_plot(self, axes, markerline):
        markerline.set_markerfacecolor('#ca3e47')
        markerline.set_markeredgecolor('#ca3e47')
        axes.set_xlabel('Failure')
        axes.set_xlim(left=0, auto=True)
        axes.set_ylim(auto=True)
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)
        axes.legend()
        plt.show()

    def get_model_strategy(self, model):
        return self.plot_strategy.get(model)

    def show_mt_warning(self, model, project_name):
        strategy = self.get_model_strategy(model)(project_name)
        strategy.show_mt_warning()
