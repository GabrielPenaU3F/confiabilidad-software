from src.data.data_repository import DataRepository
from src.domain.models.homogeneous_poisson.homogeneous_poisson_estimator import HomogeneousPoissonEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from matplotlib import pyplot as plt


class HomogeneousPoissonPlotStrategy(PlotStrategy):

    def __init__(self, project_name):
        super().__init__(project_name)

    def plot(self, project_name, lsq_params, ml_params):
        project_title = DataRepository.provide_project_data(project_name).get_project_title()
        x_axis_data = self.data.get_times()
        cumulative_failures = self.data.get_cumulative_failures()
        p = HomogeneousPoissonEstimator()

        fig, ax = plt.subplots()
        self.plot_real_data(ax, x_axis_data, cumulative_failures, project_title)
        self.plot_least_squares(ax, p, x_axis_data, lsq_params)
        self.plot_maximum_likelihood(ax, p, x_axis_data, ml_params)
        self.do_plot_format(ax)

    def plot_least_squares(self, axes, p, x_data, lsq_params):
        axes.plot(x_data,
                  p.calculate_mean_failure_numbers(x_data, lsq_params[0]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, p, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, p.calculate_mean_failure_numbers(x_data, ml_params[0]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')