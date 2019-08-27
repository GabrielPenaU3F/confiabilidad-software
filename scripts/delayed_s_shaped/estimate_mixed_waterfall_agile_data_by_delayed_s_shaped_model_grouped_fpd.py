from src.fitters.fitter import GroupedFailuresPerDayFitter

fitter = GroupedFailuresPerDayFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results()
