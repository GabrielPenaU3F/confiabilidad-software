from colorama import Fore

from src.domain.result_presenter.result_presenter import ResultPresenter


class StageResultPresenter(ResultPresenter):

    def display_data(self, number, stage):
        self.print_stage_title(number, stage)
        displaying_strategy = self.get_model_strategy(stage.get_model())()
        displaying_strategy.display_stage_results(stage)

    def print_stage_title(self, number, stage):
        print((Fore.YELLOW + 'Stage ') + (Fore.YELLOW + str(number)) + " - " +
              (Fore.YELLOW + 'From t = ') + (Fore.YELLOW + str(stage.get_initial_t())) +
              (Fore.YELLOW + ' to t = ') + (Fore.YELLOW + str(stage.get_end_t())))
