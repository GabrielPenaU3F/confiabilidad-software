from src.fitters.fitter import GroupedCumulativeFitter, GroupedFailuresPerDayFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile')
fit.show_results()

fitter = GroupedFailuresPerDayFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile')
fit.show_results()
