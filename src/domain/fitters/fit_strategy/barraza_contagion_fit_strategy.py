from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.fitters.fit_strategy.fit_strategy import FitStrategy


class BarrazaContagionFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = BarrazaContagionEstimator()
        super().__init__(project_name, model)
