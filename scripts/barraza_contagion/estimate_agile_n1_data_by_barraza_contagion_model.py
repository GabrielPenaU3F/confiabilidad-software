from src.domain.fitters.fitter import Fitter

ttf_fitter = Fitter()
fit = ttf_fitter.fit('barraza-contagion', 'agile-n1')
fit.show_results(plot_mttf=True, plot_mtbf=True)
