from src.data.data_repository import DataRepository
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from matplotlib import pyplot as plt

from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoPlotStrategy(PlotStrategy):

    def plot(self, project_name, lsq_params, ml_params):
        data = DataRepository.provide_project_data(project_name)
        project_title = data.get_project_title()
        x_axis_data = data.get_times()
        cumulative_failures = data.get_cumulative_failures()
        go = GoelOkumotoEstimator()

        fig, ax = plt.subplots()
        self.plot_real_data(ax, x_axis_data, cumulative_failures, project_title)
        self.plot_least_squares(ax, go, x_axis_data, lsq_params)
        self.plot_maximum_likelihood(ax, go, x_axis_data, ml_params)
        self.do_plot_format(ax)

    def plot_maximum_likelihood(self, axes, go, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')

    def plot_least_squares(self, axes, go, x_data, lsq_params):
        axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
