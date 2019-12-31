from src.domain.result_presenter.result_presenter import ResultPresenter


class ModelResultPresenter(ResultPresenter):

    def display_data(self, project_name, model, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        displaying_strategy = self.get_model_strategy(model)(project_name)
        self.reset_console_colors()
        displaying_strategy.display(lsq_params, ml_params, prr_lsq, prr_ml, aic)

