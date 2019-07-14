from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped

datos = RepositorioDatos.proveer_datos_observados_proyecto_agile_nro_1('ttf')
inicio = 0
#fin = 6
fin = datos.get_cantidad_datos()
ttf = datos.get_tiempos_de_falla()[inicio:fin]
fallas_acumuladas = datos.get_fallas_acumuladas()[inicio:fin]

ds = EstimadorDelayedSShaped()

aprox_inicial = (1, 0.5)
params_ds_lsq = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas, aprox_inicial)

params_ds_mv = ds.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf[1:], fallas_acumuladas[-1],
                                                                                    params_ds_lsq,
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

ax.plot(ttf, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--', label='Datos reales (Agile #1)')
ax.plot(ttf, ds.calcular_numero_medio_de_fallas(ttf, params_ds_lsq[0], params_ds_lsq[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ: a=%.5f, b=%.5f' % tuple(params_ds_lsq))
if params_ds_mv is not None:
    ax.plot(ttf, ds.calcular_numero_medio_de_fallas(ttf, params_ds_mv[0], params_ds_mv[1]),
            linewidth=1, color='#58b368', linestyle='-', label='MV: a=%.5f, b=%.5f' % tuple(params_ds_mv))

ax.legend()

ax.plot()
plt.show()
