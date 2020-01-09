from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.logistic.logistic_estimator import LogisticEstimator


class LogisticPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params, **kwargs):
        self.estimator = LogisticEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params, **kwargs)
