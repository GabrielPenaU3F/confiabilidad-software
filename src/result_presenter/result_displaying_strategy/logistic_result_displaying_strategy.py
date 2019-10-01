from colorama import Fore
from src.result_presenter.result_displaying_strategy.result_displaying_strategy import ResultDisplayingStrategy


class LogisticResultDisplayingStrategy(ResultDisplayingStrategy):

    def __init__(self, project_name):
        super().__init__(project_name, 'Logistic')

    def print_least_squares_parameters(self, a_lsq, b_lsq, c_lsq):
        print(Fore.YELLOW + 'Least squares estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('c = ' + c_lsq.__str__()))
        print()

    def print_maximum_likelihood_parameters(self, a_ml, b_ml, c_ml):
        print(Fore.YELLOW + 'Maximum likelihood estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_ml.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_ml.__str__()))
        print(Fore.LIGHTRED_EX + ('c = ' + c_ml.__str__()))
        print()
