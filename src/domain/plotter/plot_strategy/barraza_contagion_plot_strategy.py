from colorama import Back, Fore

from src.data.data_repository import DataRepository
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from matplotlib import pyplot as plt


class BarrazaContagionPlotStrategy(PlotStrategy):

    def plot(self, project_name, lsq_params, ml_params):
        data = DataRepository.provide_project_data(project_name)
        project_title = data.get_project_title()
        x_axis_data = data.get_times()
        cumulative_failures = data.get_cumulative_failures()
        bc = BarrazaContagionEstimator()

        fig, ax = plt.subplots()
        self.plot_real_data(ax, x_axis_data, cumulative_failures, project_title)
        self.plot_least_squares(ax, bc, x_axis_data, lsq_params)
        self.plot_maximum_likelihood(ax, bc, x_axis_data, ml_params)
        self.do_plot_format(ax)

    def plot_maximum_likelihood(self, axes, go, x_data, ml_params):
        pass

    def plot_least_squares(self, axes, bc, x_data, lsq_params):
        axes.plot(x_data, bc.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def show_mt_warning(self):
        print(Back.LIGHTYELLOW_EX + Fore.RED + 'Be careful. Please take into account that these are '
                                               'CONDITIONAL MTTFs or MTBFs based on the given data')
