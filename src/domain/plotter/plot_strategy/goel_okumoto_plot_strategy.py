from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = GoelOkumotoEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def plot_maximum_likelihood(self, axes, go, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')

    def plot_least_squares(self, axes, go, x_data, lsq_params):
        axes.plot(x_data, go.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')
