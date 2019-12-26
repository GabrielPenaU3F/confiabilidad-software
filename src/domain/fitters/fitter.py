from abc import ABC, abstractmethod

from src.exceptions.exceptions import InvalidArgumentException
from src.domain.fitters.fit_strategy.barraza_contagion_fit_strategy import BarrazaContagionFitStrategy
from src.domain.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.domain.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.domain.fitters.fit_strategy.gompertz_fit_strategy import GompertzFitStrategy
from src.domain.fitters.fit_strategy.homogeneous_poisson_fit_strategy import HomogeneousPoissonFitStrategy
from src.domain.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy
from src.domain.fitters.fit_strategy.musa_okumoto_fit_strategy import MusaOkumotoFitStrategy


class Fitter(ABC):

    fit_strategies = {
        'poisson': HomogeneousPoissonFitStrategy,
        'musa-okumoto': MusaOkumotoFitStrategy,
        'goel-okumoto': GoelOkumotoFitStrategy,
        'delayed-s-shaped': DSFitStrategy,
        'logistic': LogisticFitStrategy,
        'barraza-contagion': BarrazaContagionFitStrategy,
        'gompertz': GompertzFitStrategy
    }

    def get_model_strategy(self, model):
        if self.fit_strategies.keys().__contains__(model):
            return self.fit_strategies.get(model)
        else:
            raise InvalidArgumentException('The requested model does not exist')

    """
    Accepted models
        Homogeneous Poisson: 'poisson'
        Musa-Okumoto: 'musa-okumoto'
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logistic: 'logistic'
        Barraza Contagion: 'barraza-contagion'
        Gompertz: 'gompertz'
    """

    @abstractmethod
    def fit(self, *args, **kwargs):
        pass

    @abstractmethod
    def decode_kwargs(self, **kwargs):
        pass
