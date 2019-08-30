from src.fitters.fitter import GroupedFPDFitter

fitter = GroupedFPDFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results()
