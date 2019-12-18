from src.domain.fitters.fitter import Fitter

ttf_fitter = Fitter()
fit = ttf_fitter.fit('gompertz', 'agile-n1')
fit.show_results()
