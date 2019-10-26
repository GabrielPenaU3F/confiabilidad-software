from src.domain.models.gompertz.gompertz_estimator import GompertzEstimator
from src.fitters.fit_strategy.fit_strategy import FitStrategy


class GompertzFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = GompertzEstimator()
        super().__init__(project_name, model)
