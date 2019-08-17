from src.fitters.fitter import GroupedCumulativeFitter, GroupedFailuresPerDayFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results()

fitter = GroupedFailuresPerDayFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results()

