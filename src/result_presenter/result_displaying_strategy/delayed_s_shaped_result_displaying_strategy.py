from colorama import Fore

from src.data.data_repository import DataRepository
from src.result_presenter.result_displaying_strategy.result_displaying_strategy import ResultDisplayingStrategy


class DelayedSShapedResultDisplayingStrategy(ResultDisplayingStrategy):

    def display(self, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        project_data = DataRepository.provide_project_data(self.project_name)
        project_title = project_data.get_project_title()
        a_lsq = lsq_params[0]
        b_lsq = lsq_params[1]
        a_ml = ml_params[0]
        b_ml = ml_params[1]

        print((Fore.YELLOW + 'Project: ') + (Fore.LIGHTRED_EX + project_title))
        print((Fore.YELLOW + 'Model: ') + (Fore.LIGHTRED_EX + 'Delayed S-Shaped'))
        print()

        print(Fore.YELLOW + 'Least squares estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_lsq.__str__()))
        print()

        print(Fore.YELLOW + 'Maximum likelihood estimates:')
        print(Fore.LIGHTRED_EX + ('a = ' + a_ml.__str__()))
        print(Fore.LIGHTRED_EX + ('b = ' + b_ml.__str__()))
        print()

        print(Fore.YELLOW + 'Predictive Risk Ratio (PRR):')
        print(Fore.LIGHTRED_EX + ('Least squares: ' + prr_lsq.__str__()))
        print(Fore.LIGHTRED_EX + ('Maximum likelihood: ' + prr_ml.__str__()))
        print()

        print(Fore.YELLOW + 'Akaike Information Criteria (AIC):')
        print(Fore.LIGHTRED_EX + aic.__str__())