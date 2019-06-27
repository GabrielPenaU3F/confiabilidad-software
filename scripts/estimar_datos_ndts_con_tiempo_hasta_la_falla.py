from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.goel_okumoto.estimador_goel_okumoto import EstimadorGoelOkumoto

datos = RepositorioDatos.proveer_datos_observados_proyecto_NTDS()
x = datos.get_tiempos_de_falla()
y = datos.get_fallas_acumuladas()

go = EstimadorGoelOkumoto()

params_go_lsq = go.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(x, y)

params_go_mv = go.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(x, params_go_lsq,
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

ax.plot(x, y, linewidth=1, color='#263859', linestyle='--', label='Datos reales')
ax.plot(x, go.calcular_numero_medio_de_fallas(x, params_go_lsq[0], params_go_lsq[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ: a=%.5f, b=%.5f' % tuple(params_go_lsq))
if params_go_mv is not None:
        ax.plot(x, go.calcular_numero_medio_de_fallas(x, params_go_mv[0], params_go_mv[1]),
                linewidth=1, color='#58b368', linestyle='-', label='MV: a=%.5f, b=%.5f' % tuple(params_go_mv))

ax.legend()

ax.plot()
plt.show()
