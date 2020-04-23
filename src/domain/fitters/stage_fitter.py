from src.data.data_formater import TTFDataFormater, FPDDataFormater
from src.domain.fitters.fitter import Fitter
from src.domain.optional_arguments import OptionalArguments
from src.exceptions.exceptions import InvalidFitException


class StageFitter(Fitter):

    def fit(self, stage, fit_strategy, data, stage_number, **kwargs):
        data_formater = self.obtain_data_formater(data.get_format())
        initial_sample = data_formater.determine_stage_initial_sample(data, stage.get_initial_t())
        end_sample = data_formater.determine_stage_end_sample(data, stage.get_end_t())
        t0 = data_formater.determine_stage_t0(data, stage.get_initial_t())
        kwargs_new = {'initial_sample': initial_sample, 'end_sample': end_sample, 't0': t0,
                      'lsq_only': kwargs.get('lsq_only')}
        initial_approx = stage.get_optional_arguments().get_initial_approx()
        if initial_approx is not None:
            kwargs_new['initial_approx'] = initial_approx
        optional_arguments = OptionalArguments(**kwargs_new)
        try:
            stage_lsq_params, stage_ml_params = fit_strategy.fit_model(optional_arguments)
            return stage.be_fitted(fit_strategy, optional_arguments, stage_lsq_params, stage_ml_params)
        except InvalidFitException as error:
            raise InvalidFitException(str('Stage ' + str(stage_number) + ': ' + error.strerror))

    def decode_kwargs(self, **kwargs):
        pass

    def obtain_data_formater(self, format):
        if format == 'ttf':
            return TTFDataFormater()
        elif format == 'fpd':
            return FPDDataFormater()
