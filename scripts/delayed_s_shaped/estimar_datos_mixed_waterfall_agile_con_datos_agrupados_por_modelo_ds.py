from colorama import Fore
from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.modelos.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped

datos_fpd = RepositorioDatos.proveer_datos_observados_proyecto_mixed_waterfall_agile('fpd')
dias = datos_fpd.get_dias()
fallas_por_dia = datos_fpd.get_fallas_por_dia()
fallas_acumuladas = datos_fpd.get_fallas_acumuladas()

ds = EstimadorDelayedSShaped()

aprox_inicial = (1, 0.5)
params_ds_mc = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(dias, fallas_acumuladas, aprox_inicial)
params_ds_mv_fallas_acumuladas_al_dia = ds.\
    estimar_parametros_por_maxima_verosimilitud_fallas_acumuladas_al_dia(dias, fallas_acumuladas, params_ds_mc,
                                                                         metodo_resolucion='krylov')
params_ds_mv_fallas_por_dia = ds.\
    estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(dias, fallas_por_dia, params_ds_mc,
                                                               metodo_resolucion='krylov')

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

ax.plot(dias, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--',
        label='Datos reales (Mixed Waterfall-Agile)')
ax.plot(dias, ds.calcular_numero_medio_de_fallas(dias, params_ds_mc[0], params_ds_mc[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='Mínimos cuadrados')
ax.plot(dias, ds.calcular_numero_medio_de_fallas(dias, params_ds_mv_fallas_acumuladas_al_dia[0],
                                                 params_ds_mv_fallas_acumuladas_al_dia[1]),
        linewidth=1, color='#1b7fbd', linestyle='-', label='Máxima verosimilitud (Acum)')
ax.plot(dias, ds.calcular_numero_medio_de_fallas(dias, params_ds_mv_fallas_por_dia[0],  params_ds_mv_fallas_por_dia[1]),
        linewidth=1, color='#58b368', linestyle='-', label='Máxima verosimilitud (FPD)')

ax.legend()

ax.plot()

print(Fore.BLUE + ('a = ' + params_ds_mc[0].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('b = ' + params_ds_mc[1].__str__() + ' (Mínimos cuadrados)'))
print(Fore.BLUE + ('a = ' + params_ds_mv_fallas_acumuladas_al_dia[0].__str__() +
                   '(Máxima verosimilitud, fallas acumuladas)'))
print(Fore.BLUE + ('b = ' + params_ds_mv_fallas_acumuladas_al_dia[1].__str__() +
                   '(Máxima verosimilitud, fallas acumuladas)'))
print(Fore.BLUE + ('a = ' + params_ds_mv_fallas_por_dia[0].__str__() + ' (Máxima verosimilitud, fallas por día)'))
print(Fore.BLUE + ('b = ' + params_ds_mv_fallas_por_dia[1].__str__() + ' (Máxima verosimilitud, fallas por día)'))

prr_mc = ds.calcular_prr(dias, fallas_acumuladas, params_ds_mc[0], params_ds_mc[1])
prr_mv_facum = ds.calcular_prr(dias, fallas_acumuladas, params_ds_mv_fallas_acumuladas_al_dia[0],
                               params_ds_mv_fallas_acumuladas_al_dia[1])
prr_mv_fpd = ds.calcular_prr(dias, fallas_acumuladas, params_ds_mv_fallas_por_dia[0], params_ds_mv_fallas_por_dia[1])
print(Fore.GREEN + ('PRR - Mínimos cuadrados: ' + prr_mc.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud (Fallas acumuladas): ' + prr_mv_facum.__str__()))
print(Fore.GREEN + ('PRR - Máxima verosimilitud (Fallas por día): ' + prr_mv_fpd.__str__()))

aic_mv_facum = ds.calcular_aic_fallas_acumuladas_al_dia(dias, fallas_acumuladas,
                                                        params_ds_mv_fallas_acumuladas_al_dia[0],
                                                        params_ds_mv_fallas_acumuladas_al_dia[1])
aic_mv_fpd = ds.calcular_aic_fallas_por_dia(dias, fallas_por_dia, params_ds_mv_fallas_por_dia[0],
                                            params_ds_mv_fallas_por_dia[1])
print(Fore.GREEN + ('AIC (Fallas acumuladas): ' + aic_mv_facum.__str__()))
print(Fore.GREEN + ('AIC (Fallas por día): ' + aic_mv_fpd.__str__()))

plt.show()