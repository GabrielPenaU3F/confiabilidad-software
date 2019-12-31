from src.domain.fit import Fit


class MultistageFit(Fit):

    def __init__(self, project_name, stages):
        super().__init__(project_name)
        self.stages = stages

    def show_results(self, **kwargs):
        for stage in self.stages:
            stage_presenter = MultistageResultPresenter()
            stage_presenter.display_data(self.project_name, stage.get_model(), stage.get_lsq_params(),
                                         stage.get_ml_params())

    def get_number_of_stages(self):
        return len(self.stages)

    def get_stages(self):
        return self.stages
