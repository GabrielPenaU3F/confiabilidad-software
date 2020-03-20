from src.domain.fit import Fit
from src.domain.plotter.multistage_plotter import MultistagePlotter
from src.domain.result_presenter.multistage_result_presenter import MultistageResultPresenter


class MultistageFit(Fit):

    project_name = None
    stages = None
    prr_lsq = None
    prr_ml = None

    def __init__(self, project_name, stages):
        super().__init__(project_name)
        self.stages = stages
        self.prr_lsq = self.obtain_prr_lsq()
        if self.verify_ml_status():
            self.prr_ml = self.obtain_prr_ml()

    def show_results(self, **kwargs):
        multistage_result_presenter = MultistageResultPresenter()
        multistage_result_presenter.display_data(self.project_name, self.stages, self.prr_lsq, self.prr_ml)
        multistage_plotter = MultistagePlotter()
        multistage_plotter.plot_results(self.project_name, self.stages)

    def get_number_of_stages(self):
        return len(self.stages)

    def get_stages(self):
        return self.stages

    def get_prr_lsq(self):
        return self.prr_lsq

    def get_prr_ml(self):
        return self.prr_ml

    def obtain_prr_lsq(self):
        prr = 0
        for stage in self.stages:
            stage_fit_strategy = stage.get_fit_strategy()
            stage_prr = stage_fit_strategy.calculate_stage_prr(stage.get_optional_arguments(), *stage.get_lsq_params())
            prr += stage_prr
        return prr

    def obtain_prr_ml(self):
        prr = 0
        for stage in self.stages:
            stage_fit_strategy = stage.get_fit_strategy()
            stage_prr = stage_fit_strategy.calculate_stage_prr(stage.get_optional_arguments(), *stage.get_ml_params())
            prr += stage_prr
        return prr

    def verify_ml_status(self):
        for stage in self.stages:
            if not stage.verify_ml_status():
                return False
        return True
