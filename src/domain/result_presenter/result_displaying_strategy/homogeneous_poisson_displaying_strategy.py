from colorama import Fore
from src.domain.result_presenter.result_displaying_strategy.result_displaying_strategy import ResultDisplayingStrategy


class HomogeneousPoissonResultDisplayingStrategy(ResultDisplayingStrategy):

    def __init__(self, project_name):
        super().__init__(project_name, 'Poisson')

    def print_least_squares_parameters(self, *lsq_params):
        lambda_lsq = lsq_params[0]
        print(Fore.YELLOW + 'Least squares estimates:')
        print(Fore.LIGHTRED_EX + ('\u03BB = ' + lambda_lsq.__str__()))
        print()

    def print_maximum_likelihood_parameters(self, *ml_params):
        lambda_ml = ml_params[0]
        print(Fore.YELLOW + 'Maximum likelihood estimates:')
        print(Fore.LIGHTRED_EX + ('\u03BB = ' + lambda_ml.__str__()))
        print()
