from src.fitters.fitter import Fitter


class TTFFitter(Fitter):

    def choose_fitter(self, fit_strategy):
        return fit_strategy.fit_ttf()
