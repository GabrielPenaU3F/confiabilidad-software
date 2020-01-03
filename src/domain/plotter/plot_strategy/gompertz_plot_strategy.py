from src.domain.models.gompertz.gompertz_estimator import GompertzEstimator
from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy


class GompertzPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = GompertzEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)
