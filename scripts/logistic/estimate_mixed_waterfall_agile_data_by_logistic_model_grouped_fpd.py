from src.fitters.fitter import GroupedFailuresPerDayFitter

fitter = GroupedFailuresPerDayFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile')
fit.show_results()
