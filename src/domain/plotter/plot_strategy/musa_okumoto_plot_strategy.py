from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.musa_okumoto.musa_okumoto_estimator import MusaOkumotoEstimator


class MusaOkumotoPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = MusaOkumotoEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def plot_maximum_likelihood(self, axes, mo, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, mo.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')

    def plot_least_squares(self, axes, mo, x_data, lsq_params):
        axes.plot(x_data, mo.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
