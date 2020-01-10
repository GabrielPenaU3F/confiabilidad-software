from colorama import Fore

from src.domain.result_presenter.result_presenter import ResultPresenter
from src.domain.result_presenter.stage_result_presenter import StageResultPresenter


class MultistageResultPresenter(ResultPresenter):

    def display_data(self, project_name, stages, prr_lsq, prr_ml):
        self.print_project_name(project_name)
        for i in range(len(stages)):
            stage = stages[i]
            stage_presenter = StageResultPresenter()
            stage_presenter.display_data(i+1, stage)
        print((Fore.YELLOW + '-----------------------------') + "\n")
        self.print_prr(prr_lsq, prr_ml)
