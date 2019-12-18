from src.domain.fitters.fitter import Fitter

fpd_fitter = Fitter()
fit = fpd_fitter.fit('barraza-contagion', 'agile-n2')
fit.show_results()
