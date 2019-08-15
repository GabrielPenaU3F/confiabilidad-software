from src.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator
from matplotlib import pyplot as plt


class DSPlotStrategy(PlotStrategy):

    def plot(self, project_name, lsq_params, ml_params, data):
        x_axis_data = data.get_data()
        cumulative_failures = data.get_cumulative_failures()
        ds = DelayedSShapedEstimator()

        fig, ax = plt.subplots()
        ax.plot(x_axis_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
                label='Real data (' + project_name + ')')
        ax.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, lsq_params[0], lsq_params[1]),
                linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
        ax.plot(x_axis_data, ds.calculate_mean_failure_numbers(x_axis_data, ml_params[0], ml_params[1]),
                linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood (Time to failure)')
        self.do_plot_format(ax)
