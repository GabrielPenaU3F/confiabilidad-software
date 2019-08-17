from src.fitters.fitter import GroupedCumulativeFitter

fitter = GroupedCumulativeFitter()
fit = fitter.fit('delayed-s-shaped', 'mixed-waterfall-agile')
fit.show_results()

"""
params_ds_mv_fallas_por_dia = ds.\
    estimate_grouped_fpd_parameters_by_maximum_likelihood(dias, fallas_por_dia, params_ds_mc,
                                                          solving_method='krylov')
"""
