from src.data.data_repository import DataRepository
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from matplotlib import pyplot as plt


class DSPlotStrategy(PlotStrategy):

    def plot(self, project_name, lsq_params, ml_params):
        data = DataRepository.provide_project_data(project_name)
        project_title = data.get_project_title()
        x_axis_data = data.get_times()
        cumulative_failures = data.get_cumulative_failures()
        ds = DelayedSShapedEstimator()

        fig, ax = plt.subplots()
        self.plot_real_data(ax, x_axis_data, cumulative_failures, project_title)
        self.plot_least_squares(ax, ds, x_axis_data, lsq_params)
        ax.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, ml_params[0], ml_params[1]),
                linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
        self.do_plot_format(ax)

    def plot_least_squares(self, axes, ds, x_data, lsq_params):
        axes.plot(x_data, ds.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, ds, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, ds.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
