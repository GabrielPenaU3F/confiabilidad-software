from src.fitters.fitter import GroupedFPDFitter

fitter = GroupedFPDFitter()
fit = fitter.fit('gompertz', 'mixed-waterfall-agile')
fit.show_results()
