from colorama import Fore

from src.result_presenter.result_displaying_strategy.result_displaying_strategy import ResultDisplayingStrategy


class BarrazaContagionResultDisplayingStrategy(ResultDisplayingStrategy):

    def __init__(self, project_name):
        super().__init__(project_name, 'Barraza Contagion')

    def print_least_squares_parameters(self, a_lsq, b_lsq):
        print(Fore.YELLOW + 'Least squares estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_lsq.__str__()))
        print()

    def print_maximum_likelihood_parameters(self, *ml_params):
        pass
