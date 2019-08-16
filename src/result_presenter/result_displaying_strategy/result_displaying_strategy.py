from abc import ABC, abstractmethod


class ResultDisplayingStrategy(ABC):

    def __init__(self, project_name):
        self.project_name = project_name

    @abstractmethod
    def display(self, lsq_params, ml_params, prr_lsq, prr_ml, aic):
        pass

