from colorama import Fore
from matplotlib import pyplot as plt

from data.data_repository import DataRepository
from src.domain.models.delayed_s_shaped.delayed_s_shaped_estimator import DelayedSShapedEstimator

datos_fpd = DataRepository.proveer_datos_observados_proyecto_mixed_waterfall_agile('fpd')
dias = datos_fpd.get_dias()
fallas_por_dia = datos_fpd.get_fallas_por_dia()
fallas_acumuladas = datos_fpd.calculate_cumulative_failures()

ds = DelayedSShapedEstimator()

aprox_inicial = (1, 0.5)
params_ds_mc = ds.fit_mean_failure_number_by_least_squares(dias, fallas_acumuladas, aprox_inicial)
params_ds_mv_fallas_acumuladas_al_dia = ds.\
    estimate_grouped_cumulative_parameters_by_maximum_likelihood(dias, fallas_acumuladas, params_ds_mc,
                                                                 solving_method='krylov')
params_ds_mv_fallas_por_dia = ds.\
    estimate_grouped_fpd_parameters_by_maximum_likelihood(dias, fallas_por_dia, params_ds_mc,
                                                          solving_method='krylov')

fig, ax = plt.subplots()

ax.set_xlabel('Tiempo (días)')
ax.set_ylabel('Número de fallas')
ax.set_xlim(left=0, auto=True)
ax.set_ylim(bottom=-2, top=2, auto=True)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_edgecolor('black')
ax.patch.set_linewidth('1')
ax.set_facecolor("#ffffff")
ax.grid(color='black', linestyle='--', linewidth=0.5)

ax.plot(dias, fallas_acumuladas, )
ax.plot(dias, ds.calculate_mean_failure_numbers(dias, params_ds_mc[0], params_ds_mc[1]), )
ax.plot(dias, ds.calculate_mean_failure_numbers(dias, params_ds_mv_fallas_acumuladas_al_dia[0],
                                                params_ds_mv_fallas_acumuladas_al_dia[1]), )
ax.plot(dias, ds.calculate_mean_failure_numbers(dias, params_ds_mv_fallas_por_dia[0], params_ds_mv_fallas_por_dia[1]), )

ax.legend()

ax.plot(,

print(Fore.BLUE + ('a = ' + params_ds_mc[0].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('b = ' + params_ds_mc[1].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('a = ' + params_ds_mv_fallas_acumuladas_al_dia[0].__str__() +
                   '(Máxima verosimilitud, fallas acumuladas)'))
print(Fore.BLUE + ('b = ' + params_ds_mv_fallas_acumuladas_al_dia[1].__str__() +
                   '(Máxima verosimilitud, fallas acumuladas)'))
print(Fore.BLUE + ('a = ' + params_ds_mv_fallas_por_dia[0].__str__() + ' (Máxima verosimilitud, fallas por día)'))
print(Fore.BLUE + ('b = ' + params_ds_mv_fallas_por_dia[1].__str__() + ' (Máxima verosimilitud, fallas por día)'))

prr_mc = ds.calculate_prr()
prr_mv_facum = ds.calculate_prr()
prr_mv_fpd = ds.calculate_prr()
print(Fore.GREEN + ('PRR - Mínimos cuadrados: ' + prr_mc.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud (Fallas acumuladas): ' + prr_mv_facum.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud (Fallas por día): ' + prr_mv_fpd.__str__()))

aic_mv_facum = ds.calculate_grouped_cumulative_aic(dias, fallas_acumuladas,
                                                   params_ds_mv_fallas_acumuladas_al_dia[0],
                                                   params_ds_mv_fallas_acumuladas_al_dia[1])
aic_mv_fpd = ds.calculate_grouped_fpd_aic(dias, fallas_por_dia, params_ds_mv_fallas_por_dia[0],
                                          params_ds_mv_fallas_por_dia[1])
print(Fore.GREEN + ('AIC (Fallas acumuladas): ' + aic_mv_facum.__str__()))
print(Fore.GREEN + ('AIC (Fallas por día): ' + aic_mv_fpd.__str__()))

plt.show()