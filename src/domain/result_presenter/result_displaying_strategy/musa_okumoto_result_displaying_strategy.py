from colorama import Fore
from src.domain.result_presenter.result_displaying_strategy.result_displaying_strategy import ResultDisplayingStrategy


class MusaOkumotoResultDisplayingStrategy(ResultDisplayingStrategy):

    def __init__(self):
        super().__init__('Musa-Okumoto')

    def print_least_squares_parameters(self, a_lsq, b_lsq):
        print(Fore.YELLOW + 'Least squares estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_lsq.__str__()))
        print()

    def print_maximum_likelihood_parameters(self, *ml_params):
        a_ml, b_ml = ml_params
        print(Fore.YELLOW + 'Maximum likelihood estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_ml.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_ml.__str__()))
        print()
