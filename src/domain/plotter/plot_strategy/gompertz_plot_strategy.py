from src.domain.models.gompertz.gompertz_estimator import GompertzEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class GompertzPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        g = GompertzEstimator()
        self.plot_least_squares(axes, g, times, lsq_params)
        self.plot_maximum_likelihood(axes, g, times, ml_params)
        self.do_plot_format(axes)

    def plot_least_squares(self, axes, g, x_data, lsq_params):
        axes.plot(x_data,
                  g.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1], lsq_params[2]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, g, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, g.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1], ml_params[2]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
