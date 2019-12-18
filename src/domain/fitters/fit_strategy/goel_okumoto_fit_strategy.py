from src.domain.fitters.fit_strategy.fit_strategy import FitStrategy
from src.domain.models.goel_okumoto.goel_okumoto_estimator import GoelOkumotoEstimator


class GoelOkumotoFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = GoelOkumotoEstimator()
        super().__init__(project_name, model)

