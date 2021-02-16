from src.domain.fit import Fit
from src.domain.plotter.model_plotter import ModelPlotter
from src.domain.result_presenter.model_result_presenter import ModelResultPresenter


class ModelFit(Fit):

    project_name = None
    mttf = None

    def __init__(self, model_name, fit_strategy, lsq_params, ml_params, optional_arguments):
        project_name = fit_strategy.get_project_name()
        super().__init__(project_name)
        self.model = model_name
        self.fit_strategy = fit_strategy
        self.lsq_params = lsq_params
        self.ml_params = ml_params
        self.prr_lsq = fit_strategy.calculate_prr(*lsq_params)
        self.optional_arguments = optional_arguments

        if self.ml_params is not None:
            self.prr_ml = fit_strategy.calculate_prr(*ml_params)
            self.aic = fit_strategy.calculate_aic(*ml_params)
        else:
            self.prr_ml = None
            self.aic = None

        if optional_arguments.get_mts_flag() is True:
            mt_type = optional_arguments.get_mt_formula()
            if mt_type == 'conditional':
                self.mttf = fit_strategy.calculate_conditional_mttfs(*lsq_params)
                self.mtbf = fit_strategy.calculate_conditional_mtbfs(*lsq_params)
            else:
                self.mttf = fit_strategy.calculate_regular_mttfs(*lsq_params)
                self.mtbf = fit_strategy.calculate_regular_mtbfs(self.mttf)

    def show_results(self, **kwargs):
        if self.project_name is not None:
            presenter = ModelResultPresenter()
            presenter.display_data(self.project_name, self.model,
                                   self.lsq_params, self.ml_params, self.prr_lsq, self.prr_ml, self.aic)

            plotter = ModelPlotter()
            plotter.plot_results(self.project_name, self.model, self.lsq_params, self.ml_params,
                                 self.optional_arguments)
            if kwargs.get("plot_mttf") is True:
                plotter.show_mt_warning(self.model)
                plotter.plot_mttf(self.mttf)
            if kwargs.get("plot_mtbf") is True:
                plotter.show_mt_warning(self.model)
                plotter.plot_mtbf(self.mtbf)

    def get_lsq_parameters(self):
        return self.lsq_params

    def get_ml_parameters(self):
        return self.ml_params

    def get_prr_lsq(self):
        return self.prr_lsq

    def get_prr_ml(self):
        return self.prr_ml

    def get_aic(self):
        return self.aic

    def get_all_mttf(self):
        return self.mttf

    def get_all_mtbf(self):
        return self.mtbf

    def get_mttf(self, k):
        return self.mttf[k-1]

    def get_mtbf(self, k):
        return self.mtbf[k-1]
