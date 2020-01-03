from src.domain.models.homogeneous_poisson.homogeneous_poisson_estimator import HomogeneousPoissonEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class HomogeneousPoissonPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        p = HomogeneousPoissonEstimator()
        self.plot_least_squares(axes, p, times, lsq_params)
        self.plot_maximum_likelihood(axes, p, times, ml_params)
        self.do_plot_format(axes)

    def plot_least_squares(self, axes, p, x_data, lsq_params):
        axes.plot(x_data,
                  p.calculate_mean_failure_numbers(x_data, lsq_params[0]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, p, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, p.calculate_mean_failure_numbers(x_data, ml_params[0]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
