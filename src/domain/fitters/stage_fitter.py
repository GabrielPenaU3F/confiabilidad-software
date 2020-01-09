import numpy as np

from src.domain.fitters.fitter import Fitter
from src.domain.optional_arguments import OptionalArguments
from src.exceptions.exceptions import InvalidFitException


class StageFitter(Fitter):

    def fit(self, stage, fit_strategy, data, stage_number, **kwargs):
        initial_sample = self.determine_initial_sample(data, stage.get_initial_t())
        end_sample = self.determine_end_sample(data, stage.get_end_t())
        t0 = self.determine_t0(data, stage.get_initial_t())
        kwargs = {'initial_sample': initial_sample, 'end_sample': end_sample, 't0': t0}
        optional_arguments = OptionalArguments(**kwargs)
        try:
            stage_lsq_params, stage_ml_params = fit_strategy.fit_model(optional_arguments)
            return stage.be_fitted(stage_lsq_params, stage_ml_params)
        except InvalidFitException as error:
            raise InvalidFitException('Stage ' + str(stage_number) + ': ' + error.strerror)

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