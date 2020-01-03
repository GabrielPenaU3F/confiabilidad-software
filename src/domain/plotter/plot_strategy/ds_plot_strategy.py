from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator


class DSPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = DelayedSShapedEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def plot_least_squares(self, axes, ds, x_data, lsq_params):
        axes.plot(x_data, ds.calculate_mean_failure_numbers(x_data, lsq_params[0], lsq_params[1]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, ds, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, ds.calculate_mean_failure_numbers(x_data, ml_params[0], ml_params[1]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
