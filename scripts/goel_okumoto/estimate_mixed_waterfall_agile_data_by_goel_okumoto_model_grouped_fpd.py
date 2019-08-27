from src.fitters.fitter import GroupedFailuresPerDayFitter

fitter = GroupedFailuresPerDayFitter()
fit = fitter.fit('goel-okumoto', 'mixed-waterfall-agile')
fit.show_results()
