from src.domain.fitters.fitter import Fitter

fitter = Fitter()
fit = fitter.fit('gompertz', 'mixed-waterfall-agile')
fit.show_results(plot_mttf=True, plot_mtbf=True)
