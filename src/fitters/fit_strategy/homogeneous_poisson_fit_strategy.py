from src.domain.models.homogeneous_poisson.homogeneous_poisson_estimator import HomogeneousPoissonEstimator
from src.fitters.fit_strategy.fit_strategy import FitStrategy


class HomogeneousPoissonFitStrategy(FitStrategy):

    def __init__(self, project_name):
        model = HomogeneousPoissonEstimator()
        super().__init__(project_name, model)

