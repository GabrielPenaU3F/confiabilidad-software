from colorama import Back, Fore
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class BarrazaContagionPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = BarrazaContagionEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def plot_maximum_likelihood(self, axes, go, x_data, ml_params):
        pass

    def plot_least_squares(self, axes, bc, x_data, lsq_params):
        axes.plot(x_data, bc.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def show_mt_warning(self):
        print(Back.LIGHTYELLOW_EX + Fore.RED + 'Be careful. Please take into account that these are '
                                               'CONDITIONAL MTTFs or MTBFs based on the given data')
