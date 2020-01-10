from src.domain.result_presenter.result_presenter import ResultPresenter


class ModelResultPresenter(ResultPresenter):

    def display_data(self, project_name, model, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        self.print_project_name(project_name)
        displaying_strategy = self.get_model_strategy(model)()
        displaying_strategy.display_model_results(lsq_params, ml_params)
        self.print_prr(prr_lsq, prr_ml)
        self.print_aic(aic)
