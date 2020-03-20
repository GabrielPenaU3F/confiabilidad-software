from src.data.data_repository import DataRepository
from src.domain.fitters.fitter import Fitter
from src.domain.fitters.stage_fitter import StageFitter
from src.domain.optional_arguments import OptionalArguments
from src.domain.stage import Stage
from src.domain.multistage_fit import MultistageFit
from src.exceptions.exceptions import InvalidStageDefinitionException


class MultistageFitter(Fitter):

    def __init__(self):
        self.stages = []

    def add_stage(self, initial_t, end_t, model, **kwargs):
        self.check_for_time_consistency(initial_t)
        optional_arguments = self.decode_kwargs(**kwargs)
        stage = Stage(initial_t, end_t, model, optional_arguments)
        self.stages.append(stage)

    def fit(self, project_name, **kwargs):
        fitted_stages = []
        for i in range(len(self.stages)):
            stage = self.stages[i]
            fit_strategy = self.get_model_strategy(stage.get_model())(project_name)
            data = DataRepository.provide_project_data(project_name)
            stage_number = i + 1
            stage_fitter = StageFitter()
            fitted_stage = stage_fitter.fit(stage, fit_strategy, data, stage_number, **kwargs)
            fitted_stages.append(fitted_stage)
        return MultistageFit(project_name, fitted_stages)

    def decode_kwargs(self, **kwargs):
        return OptionalArguments(**kwargs)

    def check_for_time_consistency(self, initial_t):
        if len(self.stages) > 0 and initial_t != self.stages[-1].get_end_t():
            raise InvalidStageDefinitionException(
                'The added stage must begin at the same t where the previous stage ends')
