from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.fitters.fit_strategy.fit_strategy import FitStrategy


class BarrazaContagionFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = BarrazaContagionEstimator()
        super().__init__(project_name, model)

    def calculate_mttfs(self, *model_parameters):
        if self.data.get_format() == 'ttf':
            return self.model.calculate_mttfs(self.data.get_data(), *model_parameters)
        else:
            return None
