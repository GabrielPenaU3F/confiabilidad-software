from colorama import Back, Fore
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class BarrazaContagionPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = BarrazaContagionEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def show_mt_warning(self):
        print("\n" + Back.LIGHTYELLOW_EX + Fore.RED + 'Be careful. Please take into account that these are '
              'CONDITIONAL MTTFs or MTBFs based on the given data')
