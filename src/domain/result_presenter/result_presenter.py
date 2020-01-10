from abc import ABC, abstractmethod

from colorama import Back, Fore

from src.data.data_repository import DataRepository
from src.domain.result_presenter.result_displaying_strategy.barraza_contagion_result_displaying_strategy import \
    BarrazaContagionResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.delayed_s_shaped_result_displaying_strategy import \
    DelayedSShapedResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.goel_okumoto_result_display_strategy import \
    GoelOkumotoResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.gompertz_result_displaying_strategy import \
    GompertzResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.homogeneous_poisson_displaying_strategy import \
    HomogeneousPoissonResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.logistic_result_displaying_strategy import \
    LogisticResultDisplayingStrategy
from src.domain.result_presenter.result_displaying_strategy.musa_okumoto_result_displaying_strategy import \
    MusaOkumotoResultDisplayingStrategy


class ResultPresenter(ABC):

    result_displaying_strategy = {
        'poisson': HomogeneousPoissonResultDisplayingStrategy,
        'musa-okumoto': MusaOkumotoResultDisplayingStrategy,
        'goel-okumoto': GoelOkumotoResultDisplayingStrategy,
        'delayed-s-shaped': DelayedSShapedResultDisplayingStrategy,
        'logistic': LogisticResultDisplayingStrategy,
        'barraza-contagion': BarrazaContagionResultDisplayingStrategy,
        'gompertz': GompertzResultDisplayingStrategy
    }

    @abstractmethod
    def display_data(self, *args):
        pass

    def print_project_name(self, project_name):
        self.reset_console_colors()
        project_data = DataRepository.provide_project_data(project_name)
        project_title = project_data.get_project_title()
        print((Fore.YELLOW + 'Project: ') + (Fore.LIGHTRED_EX + project_title) + "\n")

    def reset_console_colors(self):
        print(Back.RESET + Fore.RESET)

    def get_model_strategy(self, model):
        return self.result_displaying_strategy.get(model)

    def print_prr(self, prr_lsq, prr_ml):
        print(Fore.YELLOW + 'Predictive Risk Ratio (PRR):')
        print(Fore.LIGHTRED_EX + ('Least squares: ' + prr_lsq.__str__()))
        if prr_ml is not None:
            print(Fore.LIGHTRED_EX + ('Maximum likelihood: ' + prr_ml.__str__()))
            print()

    def print_aic(self, aic):
        if aic is not None:
            print(Fore.YELLOW + 'Akaike Information Criteria (AIC):')
            print(Fore.LIGHTRED_EX + aic.__str__())
            print()
