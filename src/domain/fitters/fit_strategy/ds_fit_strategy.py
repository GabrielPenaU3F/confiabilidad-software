from src.domain.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator


class DSFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = DelayedSShapedEstimator()
        super().__init__(project_name, model)
