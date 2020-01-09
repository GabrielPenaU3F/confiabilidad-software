from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params, **kwargs):
        self.estimator = GoelOkumotoEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params, **kwargs)
