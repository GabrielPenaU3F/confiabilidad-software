from src.domain.models.homogeneous_poisson.homogeneous_poisson_estimator import HomogeneousPoissonEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class HomogeneousPoissonPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = HomogeneousPoissonEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)
