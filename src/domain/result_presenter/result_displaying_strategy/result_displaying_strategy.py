from abc import ABC, abstractmethod

from colorama import Fore


class ResultDisplayingStrategy(ABC):

    def __init__(self, model_title):
        self.model_title = model_title

    def display_model_results(self, lsq_params, ml_params):
        self.print_model(self.model_title)
        self.print_least_squares_parameters(*lsq_params)
        if ml_params is not None:
            self.print_maximum_likelihood_parameters(*ml_params)


    def display_stage_results(self, stage):
        self.print_model(self.model_title)
        self.print_least_squares_parameters(*stage.get_lsq_params())
        self.print_maximum_likelihood_parameters(*stage.get_ml_params())

    def print_model(self, model_title):
        print((Fore.YELLOW + 'Model: ') + (Fore.LIGHTRED_EX + model_title) + "\n")

    @abstractmethod
    def print_least_squares_parameters(self, *lsq_params):
        pass

    @abstractmethod
    def print_maximum_likelihood_parameters(self, *ml_params):
        pass


