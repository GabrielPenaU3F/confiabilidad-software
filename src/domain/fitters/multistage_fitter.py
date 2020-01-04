import numpy as np

from src.data.data_repository import DataRepository
from src.domain.fitters.fitter import Fitter
from src.domain.fitters.optional_arguments import OptionalArguments
from src.domain.fitters.stage import Stage
from src.domain.multistage_fit import MultistageFit
from src.exceptions.exceptions import InvalidStageDefinitionException


class MultistageFitter(Fitter):

    def __init__(self):
        self.stages = []

    def add_stage(self, initial_t, end_t, model):
        self.check_for_time_consistency(initial_t)
        stage = Stage(initial_t, end_t, model)
        self.stages.append(stage)

    def fit(self, project_name):
        for stage in self.stages:
            fit_strategy = self.get_model_strategy(stage.get_model())(project_name)
            data = DataRepository.provide_project_data(project_name)
            initial_sample = self.determine_initial_sample(data, stage.get_initial_t())
            end_sample = self.determine_end_sample(data, stage.get_end_t())
            t0 = self.determine_t0(data, stage.get_initial_t())
            kwargs = {
                'initial_sample': initial_sample,
                'end_sample': end_sample,
                't0': t0
            }
            stage_lsq_params, stage_ml_params = fit_strategy.fit_model(OptionalArguments(**kwargs))
            stage.set_lsq_params(stage_lsq_params)
            stage.set_ml_params(stage_ml_params)
        return MultistageFit(project_name, self.stages)

    def decode_kwargs(self, **kwargs):
        pass

    def determine_end_sample(self, data, end_t):
        format = data.get_format()
        if format == 'ttf':
            ttfs = data.get_data()
            for i in range(len(ttfs)):
                if ttfs[i] > end_t:
                    return i - 1
            return len(ttfs) - 1
        elif format == 'grouped':
            pass

    def determine_initial_sample(self, data, initial_t):
        format = data.get_format()
        if format == 'ttf':
            ttfs = data.get_data()
            for i in range(len(ttfs)):
                if ttfs[i] >= initial_t:
                    return i
        elif format == 'grouped':
            pass

    def determine_t0(self, data, initial_t):
        format = data.get_format()
        if format == 'ttf':
            ttfs = list(np.copy(data.get_data()))
            ttfs.insert(0, 0)
            for i in range(len(ttfs)):
                if ttfs[i] > initial_t:
                    return ttfs[i - 1]
        elif format == 'grouped':
            pass

    def check_for_time_consistency(self, initial_t):
        if len(self.stages) > 0 and initial_t != self.stages[-1].get_end_t():
            raise InvalidStageDefinitionException(
                'The added stage must begin at the same t where the previous stage ends')
