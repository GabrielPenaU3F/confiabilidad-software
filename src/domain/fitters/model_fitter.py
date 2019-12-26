from colorama import Back, Fore
from src.domain.model_fit import ModelFit
from src.domain.fitters.fitter import Fitter
from src.domain.fitters.optional_arguments import OptionalArguments


class ModelFitter(Fitter):

    def fit(self, model, project_name, **kwargs):
        optional_arguments = self.decode_kwargs(**kwargs)
        try:
            fit_strategy = self.get_model_strategy(model)(project_name)
            lsq_params, ml_params = fit_strategy.fit_model(optional_arguments)
            return ModelFit(model, fit_strategy, lsq_params, ml_params, optional_arguments)
        except TypeError as error:
            print(Back.LIGHTYELLOW_EX + Fore.RED + str(error))
            return ModelFit(None, None, None, None, None)

    def decode_kwargs(self, **kwargs):
        return OptionalArguments(**kwargs)
