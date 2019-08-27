from src.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile', cumulative=True)
fit.show_results()
