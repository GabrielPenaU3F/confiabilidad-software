from src.domain.plotter.plot_strategy.plot_strategy import PlotStrategy
from src.domain.models.musa_okumoto.musa_okumoto_estimator import MusaOkumotoEstimator


class MusaOkumotoPlotStrategy(PlotStrategy):

    def plot(self, axes, times, cumulative_failures, lsq_params, ml_params):
        self.estimator = MusaOkumotoEstimator()
        super().plot(axes, times, cumulative_failures, lsq_params, ml_params)
