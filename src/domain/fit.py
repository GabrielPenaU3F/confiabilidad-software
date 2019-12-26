from abc import ABC, abstractmethod


class Fit(ABC):

    def __init__(self, project_name):
        self.project_name = project_name

    @abstractmethod
    def show_results(self, **kwargs):
        pass
