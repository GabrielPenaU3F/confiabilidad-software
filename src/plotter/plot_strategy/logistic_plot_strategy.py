from data.data_repository import DataRepository
from src.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.models.logistic.logistic_estimator import LogisticEstimator
from matplotlib import pyplot as plt


class LogisticPlotStrategy(PlotStrategy):

    def __init__(self, project_name):
        super().__init__(project_name)

    def plot(self, project_name, lsq_params, ml_params):
        project_title = DataRepository.provide_project_data(project_name).get_project_title()
        x_axis_data = self.data.get_data()
        cumulative_failures = self.data.get_cumulative_failures()
        log = LogisticEstimator()

        fig, ax = plt.subplots()
        ax.plot(x_axis_data, cumulative_failures, linewidth=1, color='#263859', linestyle='--',
                label='Real data (' + project_title + ')')
        ax.plot(x_axis_data, log.calculate_mean_failure_numbers(x_axis_data, lsq_params[0], lsq_params[1], lsq_params[2]),
                linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
        ax.plot(x_axis_data, log.calculate_mean_failure_numbers(x_axis_data, ml_params[0], ml_params[1], ml_params[2]),
                linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood (Time to failure)')
        self.do_plot_format(ax)
