from src.data.data_repository import DataRepository
from src.domain.fitters.fitter import Fitter
from src.domain.fitters.optional_arguments import OptionalArguments
from src.domain.fitters.stage import Stage
from src.domain.multistage_fit import MultistageFit


class MultistageFitter(Fitter):

    def __init__(self):
        self.stages = []

    def add_stage(self, initial_t, end_t, model):
        stage = Stage(initial_t, end_t, model)
        self.stages.append(stage)

    def fit(self, project_name):
        for stage in self.stages:
            fit_strategy = self.get_model_strategy(stage.get_model())(project_name)
            kwargs = {'t0': stage.get_initial_t(),
                      'end_sample': self.determine_end_sample(project_name, stage.get_end_t())
                      }
            stage_optional_arguments = OptionalArguments(**kwargs)
            stage_lsq_params, stage_ml_params = fit_strategy.fit_model(stage_optional_arguments)
            stage.set_lsq_params(stage_lsq_params)
            stage.set_ml_params(stage_ml_params)
        return MultistageFit(project_name, self.stages)

    def decode_kwargs(self, **kwargs):
        pass

    def determine_end_sample(self, project_name, end_t):
        data = DataRepository.provide_project_data(project_name)
        format = data.get_format()
        if format == 'ttf':
            ttfs = data.get_data()
            for i in range(len(ttfs)):
                if ttfs[i] > end_t:
                    return i - 1
        elif format == 'grouped':
            pass
