from src.domain.fitters.fitter import Fitter

fpd_fitter = Fitter()
fit = fpd_fitter.fit('barraza-contagion', 'mixed-waterfall-agile')
fit.show_results()
