from src.result_presenter.result_displaying_strategy.delayed_s_shaped_result_displaying_strategy import \
    DelayedSShapedResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.goel_okumoto_result_display_strategy import \
    GoelOkumotoResultDisplayingStrategy
from src.result_presenter.result_displaying_strategy.logistic_result_displaying_strategy import \
    LogisticResultDisplayingStrategy


class ResultPresenter:

    result_displaying_strategy = {
        'goel-okumoto': GoelOkumotoResultDisplayingStrategy,
        'delayed-s-shaped': DelayedSShapedResultDisplayingStrategy,
        'logistic': LogisticResultDisplayingStrategy
    }

    def display_data(self, project_name, model, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        displaying_strategy = self.get_model_strategy(model)(project_name)
        displaying_strategy.display(lsq_params, ml_params, prr_lsq, prr_ml, aic)

    def get_model_strategy(self, model):
        return self.result_displaying_strategy.get(model)
