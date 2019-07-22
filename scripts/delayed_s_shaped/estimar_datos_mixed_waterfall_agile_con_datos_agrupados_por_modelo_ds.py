from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.modelos.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped

datos_fpd = RepositorioDatos.proveer_datos_observados_proyecto_mixed_waterfall_agile('fpd')
dias = datos_fpd.get_dias()
fallas_por_dia = datos_fpd.get_fallas_por_dia()
fallas_acumuladas = datos_fpd.get_fallas_acumuladas()

ds = EstimadorDelayedSShaped()

aprox_inicial = (1, 0.5)
params_ds_lsq = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(dias, fallas_acumuladas, aprox_inicial)

params_ds_mv = ds.estimar_parametros_por_maxima_verosimilitud_fallas_acumuladas_al_dia(
    dias, fallas_acumuladas, params_ds_lsq, metodo_resolucion='krylov')

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
ax.plot(dias, ds.calcular_numero_medio_de_fallas(dias, params_ds_lsq[0], params_ds_lsq[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ: a=%.5f, b=%.5f' % tuple(params_ds_lsq))
if params_ds_mv is not None:
    ax.plot(dias, ds.calcular_numero_medio_de_fallas(dias, params_ds_mv[0], params_ds_mv[1]),
            linewidth=1, color='#58b368', linestyle='-', label='MV: a=%.5f, b=%.5f' % tuple(params_ds_mv))

ax.legend()

ax.plot()

prr = ds.calcular_prr(dias, fallas_acumuladas, params_ds_mv[0], params_ds_mv[1])
print(prr)

plt.show()
