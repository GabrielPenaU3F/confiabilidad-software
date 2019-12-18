from src.domain.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('poisson', 'ntds')
fit.show_results(plot_mttf=True, plot_mtbf=True)
