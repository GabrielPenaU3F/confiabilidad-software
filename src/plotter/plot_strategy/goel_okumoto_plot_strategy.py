from data.data_repository import DataRepository
from src.plotter.plot_strategy.plot_strategy import PlotStrategy
from matplotlib import pyplot as plt

from src.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoPlotStrategy(PlotStrategy):

    def plot(self, project_name, lsq_params, ml_params):
        data = DataRepository.provide_observed_data_from_project(project_name)
        x_axis_data = data.get_data()
        cumulative_failures = data.get_cumulative_failures()
        go = GoelOkumotoEstimator()

        fig, ax = plt.subplots()
        ax.plot(x_axis_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
                label='Real data (' + project_name + ')')
        ax.plot(x_axis_data, go.calculate_mean_failure_numbers(x_axis_data, lsq_params[0], lsq_params[1]),
                linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
        ax.plot(x_axis_data, go.calculate_mean_failure_numbers(x_axis_data, ml_params[0], ml_params[1]),
                linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood (Time to failure)')
        self.do_plot_format(ax)
