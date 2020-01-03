from src.domain.plotter.plotter import Plotter
from matplotlib import pyplot as plt

from src.domain.plotter.stage_plotter import StagePlotter


class MultistagePlotter(Plotter):

    def plot_results(self, project_name, stages):
        fig, axes = plt.subplots()
        project_title, times, cumulative_failures = self.obtain_plot_data(project_name)
        self.plot_real_data(axes, times, cumulative_failures, project_title)
        for stage in stages:
            stage_plotter = StagePlotter()
            stage_plotter.plot_results(axes, stage, times, cumulative_failures)
        plt.show()

    def plot_mttf(self, *args):
        pass

    def plot_mtbf(self, *args):
        pass
