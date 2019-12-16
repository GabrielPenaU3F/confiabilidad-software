from colorama import Back, Fore

from src.result_presenter.result_displaying_strategy.barraza_contagion_result_displaying_strategy import \
    BarrazaContagionResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.delayed_s_shaped_result_displaying_strategy import \
    DelayedSShapedResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.goel_okumoto_result_display_strategy import \
    GoelOkumotoResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.gompertz_result_displaying_strategy import \
    GompertzResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.homogeneous_poisson_displaying_strategy import \
    HomogeneousPoissonResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.logistic_result_displaying_strategy import \
    LogisticResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.musa_okumoto_result_displaying_strategy import \
    MusaOkumotoResultDisplayingStrategy


class ResultPresenter:

    result_displaying_strategy = {
        'poisson': HomogeneousPoissonResultDisplayingStrategy,
        'musa-okumoto': MusaOkumotoResultDisplayingStrategy,
        'goel-okumoto': GoelOkumotoResultDisplayingStrategy,
        'delayed-s-shaped': DelayedSShapedResultDisplayingStrategy,
        'logistic': LogisticResultDisplayingStrategy,
        'barraza-contagion': BarrazaContagionResultDisplayingStrategy,
        'gompertz': GompertzResultDisplayingStrategy
    }

    def display_data(self, project_name, model, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        displaying_strategy = self.get_model_strategy(model)(project_name)
        self.reset_console_colors()
        displaying_strategy.display(lsq_params, ml_params, prr_lsq, prr_ml, aic)

    def reset_console_colors(self):
        print(Back.RESET + Fore.RESET)

    def get_model_strategy(self, model):
        return self.result_displaying_strategy.get(model)
