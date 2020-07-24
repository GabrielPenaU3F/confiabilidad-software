from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator
from src.domain.fitters.fit_strategy.fit_strategy import FitStrategy


class BarrazaContagionFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = BarrazaContagionEstimator()
        super().__init__(project_name, model)

    def calculate_mttfs(self, optional_arguments, *model_parameters):
        mt_formula = optional_arguments.get_mt_formula()
        if self.data.get_format() == 'ttf':
            return self.model.calculate_mttfs(mt_formula, self.data, *model_parameters)
        else:
            return None

    def calculate_mtbfs(self, optional_arguments, mttfs):
        return self.model.calculate_mtbfs(mttfs)
