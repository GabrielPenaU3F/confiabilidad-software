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

params_ds_lsq = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas)

'''
        Lo que ocurre acá es insólito. Para empezar, la resolución resulta exremadamente sensible a las condiciones 
        iniciales. Poniendo algún valor ligeramente distinto, a veces te halla una solución rarísima 
        (me han aparecido, por ejemplo, valores de a negativos que daban curvas decrecientes). Como él ajuste de 
        mínimos cuadrados no converge, no se lo puede usar como input inicial, provoca que las iteraciones no lo muevan
        de ahí, es decir MV tampoco converge en ese caso. Cambiando a mano los parametros inciales di con varias 
        combinaciones que dan curvas mas o menos cercanas: [30, 0.003], [30, 0.005], [27, 0.003] por ejemplo. Pero, 
        si le varias de 30 a 31 ya te da cualquier cosa. Y muchas veces directamente encuentra overflow y corta. 
        Muy raro. Me pasó solamente con estos datos, los del NDTS andan barbaro. Tomar la parte inicial no sirve,
        son muy poquitos datos. 
'''
params_ds_mv = ds.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf[1:], fallas_acumuladas[-1],
                                                                                    [30, 0.003],
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

ax.plot(ttf, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--', label='Datos reales')
ax.plot(ttf, ds.calcular_numero_medio_de_fallas(ttf, params_ds_lsq[0], params_ds_lsq[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ: a=%.5f, b=%.5f' % tuple(params_ds_lsq))
if params_ds_mv is not None:
    ax.plot(ttf, ds.calcular_numero_medio_de_fallas(ttf, params_ds_mv[0], params_ds_mv[1]),
            linewidth=1, color='#58b368', linestyle='-', label='MV: a=%.5f, b=%.5f' % tuple(params_ds_mv))

ax.legend()

ax.plot()
plt.show()
