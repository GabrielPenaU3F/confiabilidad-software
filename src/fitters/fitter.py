from abc import ABC, abstractmethod

from colorama import Back, Fore

from src.domain.fit import Fit
from src.exceptions.exceptions import InvalidArgumentException
from src.fitters.fit_strategy.barraza_contagion_fit_strategy import BarrazaContagionFitStrategy
from src.fitters.fit_strategy.ds_fit_strategy import DSFitStrategy
from src.fitters.fit_strategy.goel_okumoto_fit_strategy import GoelOkumotoFitStrategy
from src.fitters.fit_strategy.gompertz_fit_strategy import GompertzFitStrategy
from src.fitters.fit_strategy.homogeneous_poisson_fit_strategy import HomogeneousPoissonFitStrategy
from src.fitters.fit_strategy.logistic_fit_strategy import LogisticFitStrategy
from src.fitters.fit_strategy.musa_okumoto_fit_strategy import MusaOkumotoFitStrategy
from src.fitters.format_strategy.grouped_cumulative_format_strategy import GroupedCumulativeFormatStrategy
from src.fitters.format_strategy.grouped_fpd_format_strategy import GroupedFPDFormatStrategy
from src.fitters.format_strategy.ttf_format_strategy import TTFFormatStrategy


class Fitter(ABC):

    fit_strategy = {
        'poisson': HomogeneousPoissonFitStrategy,
        'musa-okumoto': MusaOkumotoFitStrategy,
        'goel-okumoto': GoelOkumotoFitStrategy,
        'delayed-s-shaped': DSFitStrategy,
        'logistic': LogisticFitStrategy,
        'barraza-contagion': BarrazaContagionFitStrategy,
        'gompertz': GompertzFitStrategy
    }

    def get_model_strategy(self, model):
        if self.fit_strategy.keys().__contains__(model):
            return self.fit_strategy.get(model)
        else:
            raise InvalidArgumentException('The requested model does not exist')


    """
    Accepted models
        Musa-Okumoto: 'musa-okumoto'
        Goel-Okumoto: 'goel-okumoto'
        Delayed S-Shaped: 'delayed-s-shaped'
        Logistic: 'logistic'
        Barraza Contagion: 'barraza-contagion'
        Gompertz: 'gompertz'
    """
    def fit(self, model, project_name, **kwargs):

        fit_strategy = self.get_model_strategy(model)(project_name)
        try:
            format_strategy = self.choose_format_strategy(fit_strategy.get_data(), fit_strategy.get_model())
            lsq_params, ml_params = fit_strategy.fit_model(format_strategy, **kwargs)
            mts_flag = kwargs.get('mts')
            return Fit(project_name, model, fit_strategy, lsq_params, ml_params, mts_flag)
        except TypeError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            return Fit(None, None, None, None, None, None)

    @abstractmethod
    def choose_format_strategy(self, data, model):
        pass


class TTFFitter(Fitter):

    def choose_format_strategy(self, data, model):
        if data.get_format() == 'ttf':
            return TTFFormatStrategy(data, model)
        else:
            raise InvalidArgumentException('The fitter does not match the requested project\'s data format')


class GroupedCumulativeFitter(Fitter):

    def choose_format_strategy(self, data, model):
        if data.get_format() == 'grouped':
            return GroupedCumulativeFormatStrategy(data, model)
        else:
            raise InvalidArgumentException('The fitter does not match the requested project\'s data format')


class GroupedFPDFitter(Fitter):

    def choose_format_strategy(self, data, model):
        if data.get_format() == 'grouped':
            return GroupedFPDFormatStrategy(data, model)
        else:
            raise InvalidArgumentException('The fitter does not match the requested project\'s data format')
