from src.domain.plotter.plotter import Plotter
from matplotlib import pyplot as plt

from src.domain.plotter.stage_plotter import StagePlotter


class MultistagePlotter(Plotter):

    def plot_results(self, project_name, stages):
        for stage in stages:
            stage_plotter = StagePlotter()
            stage_plotter.plot_results(stage)
        plt.show()

    def plot_mttf(self, *args):
        pass

    def plot_mtbf(self, *args):
        pass
