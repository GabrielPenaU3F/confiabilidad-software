from src.domain.fitters.fitter import GroupedFPDFitter

fitter = GroupedFPDFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results(plot_mttf=True, plot_mtbf=True)
