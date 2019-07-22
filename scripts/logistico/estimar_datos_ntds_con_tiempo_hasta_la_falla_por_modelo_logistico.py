from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.modelos.logistico.estimador_logistico import EstimadorLogistico

datos = RepositorioDatos.proveer_datos_observados_proyecto_NTDS('ttf')
ttf = datos.get_tiempos_de_falla()
fallas_acumuladas = datos.get_fallas_acumuladas()

log = EstimadorLogistico()

aprox_inicial = (10, 0.05, 20)
params_log_lsq = log.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(ttf, fallas_acumuladas, aprox_inicial)

params_log_mv = log.estimar_parametros_por_maxima_verosimilitud_tiempo_hasta_la_falla(ttf, fallas_acumuladas[-1],
                                                                                      params_log_lsq,
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

ax.plot(ttf, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--', label='Datos reales (NTDS)')
ax.plot(ttf, log.calcular_numero_medio_de_fallas(ttf, params_log_lsq[0], params_log_lsq[1], params_log_lsq[2]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ: a=%.5f, b=%.5f, c=%.5f' % tuple(params_log_lsq))
if params_log_mv is not None:
    ax.plot(ttf, log.calcular_numero_medio_de_fallas(ttf, params_log_mv[0], params_log_mv[1], params_log_mv[2]),
            linewidth=1, color='#58b368', linestyle='-', label='MV: a=%.5f, b=%.5f, c=%.5f' % tuple(params_log_mv))

ax.legend()

ax.plot()

prr = log.calcular_prr(ttf, fallas_acumuladas, params_log_mv[0], params_log_mv[1], params_log_mv[2])
print(prr)

plt.show()
