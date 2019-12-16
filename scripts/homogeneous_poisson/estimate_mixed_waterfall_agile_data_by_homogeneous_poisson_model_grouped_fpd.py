from src.fitters.fitter import GroupedFPDFitter

fitter = GroupedFPDFitter()
fit = fitter.fit('poisson', 'mixed-waterfall-agile')
fit.show_results(plot_mttf=True, plot_mtbf=True)
