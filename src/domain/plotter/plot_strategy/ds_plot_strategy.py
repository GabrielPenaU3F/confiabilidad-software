from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator


class DSPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params, **kwargs):
        self.estimator = DelayedSShapedEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params, **kwargs)
