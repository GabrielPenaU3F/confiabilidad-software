from src.domain.fitters.fitter import Fitter

ttf_fitter = Fitter()
fit = ttf_fitter.fit('delayed-s-shaped', 'ntds')
fit.show_results(plot_mttf=True, plot_mtbf=True)
