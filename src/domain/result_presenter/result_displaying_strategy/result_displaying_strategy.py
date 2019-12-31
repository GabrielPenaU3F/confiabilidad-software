from abc import ABC, abstractmethod

from colorama import Fore

from src.data.data_repository import DataRepository


class ResultDisplayingStrategy(ABC):

    def __init__(self, project_name, model_title):
        self.project_name = project_name
        self.model_title = model_title

    def display_model_results(self, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        self.print_model(self.model_title)
        self.print_least_squares_parameters(*lsq_params)
        if ml_params is not None:
            self.print_maximum_likelihood_parameters(*ml_params)
        self.print_prr(prr_lsq, prr_ml)
        self.print_aic(aic)

    def print_model(self, model_title):
        print((Fore.YELLOW + 'Model: ') + (Fore.LIGHTRED_EX + model_title))
        print()

    @abstractmethod
    def print_least_squares_parameters(self, *lsq_params):
        pass

    @abstractmethod
    def print_maximum_likelihood_parameters(self, *ml_params):
        pass

    def print_prr(self, prr_lsq, prr_ml):
        print(Fore.YELLOW + 'Predictive Risk Ratio (PRR):')
        print(Fore.LIGHTRED_EX + ('Least squares: ' + prr_lsq.__str__()))
        if prr_ml is not None:
            print(Fore.LIGHTRED_EX + ('Maximum likelihood: ' + prr_ml.__str__()))
            print()

    def print_aic(self, aic):
        if aic is not None:
            print(Fore.YELLOW + 'Akaike Information Criteria (AIC):')
            print(Fore.LIGHTRED_EX + aic.__str__())
            print()

