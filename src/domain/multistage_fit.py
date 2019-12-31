from src.domain.fit import Fit
from src.domain.result_presenter.multistage_result_presenter import MultistageResultPresenter


class MultistageFit(Fit):

    def __init__(self, project_name, stages):
        super().__init__(project_name)
        self.stages = stages

    def show_results(self, **kwargs):
        multistage_result_presenter = MultistageResultPresenter()
        multistage_result_presenter.display_data(self.project_name, self.stages)

    def get_number_of_stages(self):
        return len(self.stages)

    def get_stages(self):
        return self.stages
