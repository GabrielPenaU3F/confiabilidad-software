from src.domain.plotter.plotter import Plotter
from matplotlib import pyplot as plt

from src.domain.plotter.stage_plotter import StagePlotter


class MultistagePlotter(Plotter):

    def plot_results(self, project_name, stages):
        fig, axes = plt.subplots()
        project_title, times, cumulative_failures = self.obtain_full_data(project_name)
        self.plot_real_data(axes, times, cumulative_failures, project_title)
        for i in range(len(stages)):
            stage = stages[i]
            kwargs = {}
            if i == len(stages) - 1:
                kwargs['legendless_lsq'] = True
                kwargs['legendless_ml'] = True
            stage_plotter = StagePlotter()
            stage_plotter.plot_results(axes, stage, times, cumulative_failures, **kwargs)
        plt.show()

    def plot_mttf(self, *args):
        pass

    def plot_mtbf(self, *args):
        pass
