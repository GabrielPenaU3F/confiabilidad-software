from src.domain.models.musa_okumoto.musa_okumoto_estimator import MusaOkumotoEstimator
from src.domain.fitters.fit_strategy.fit_strategy import FitStrategy


class MusaOkumotoFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = MusaOkumotoEstimator()
        super().__init__(project_name, model)

