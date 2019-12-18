from src.domain.fitters.fitter import Fitter

ttf_fitter = Fitter()
fit = ttf_fitter.fit('gompertz', 'ntds')
fit.show_results()
