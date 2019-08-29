from src.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.logistic.logistic_estimator import LogisticEstimator


class LogisticFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = LogisticEstimator()
        super().__init__(project_name, model)
