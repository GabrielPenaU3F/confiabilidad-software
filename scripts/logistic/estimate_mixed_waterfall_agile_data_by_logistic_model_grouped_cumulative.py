from src.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('logistic', 'mixed-waterfall-agile', cumulative=True)
fit.show_results()
