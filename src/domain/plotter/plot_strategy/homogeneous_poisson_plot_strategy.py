from src.domain.models.homogeneous_poisson.homogeneous_poisson_estimator import HomogeneousPoissonEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class HomogeneousPoissonPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = HomogeneousPoissonEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)

    def plot_least_squares(self, axes, p, x_data, lsq_params):
        axes.plot(x_data,
                  p.calculate_mean_failure_numbers(x_data, lsq_params[0]),
                  linewidth=1, color='#ca3e47', linestyle='-', label='Least squares')

    def plot_maximum_likelihood(self, axes, p, x_data, ml_params):
        if ml_params is not None:
            axes.plot(x_data, p.calculate_mean_failure_numbers(x_data, ml_params[0]),
                      linewidth=1, color='#58b368', linestyle='-', label='Maximum likelihood')
