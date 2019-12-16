from src.fitters.fitter import TTFFitter

ttf_fitter = TTFFitter()
fit = ttf_fitter.fit('poisson', 'agile-n1')
fit.show_results(plot_mttf=True, plot_mtbf=True)
