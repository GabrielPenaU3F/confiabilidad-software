from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.modelos.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped
from src.modelos.goel_okumoto.estimador_goel_okumoto import EstimadorGoelOkumoto

datos_fpd = RepositorioDatos.proveer_datos_observados_proyecto_mixed_waterfall_agile('fpd')
dias = datos_fpd.get_dias()
fallas_por_dia = datos_fpd.get_fallas_por_dia()
fallas_acumuladas = datos_fpd.calcular_fallas_acumuladas()

# Se estima con el modelo DS entre los días 1 y 100 y con Goel-Okumoto a partir del 101.

go = EstimadorGoelOkumoto()
ds = EstimadorDelayedSShaped()

# De 0 a 100
aprox_inicial_ds = (1, 0.5)
dias_etapa1 = dias[0:99]
fallas_por_dia_etapa1 = fallas_por_dia[0:99]
fallas_acumuladas_etapa1 = fallas_acumuladas[0:99]

params_ds_lsq_etapa_1 = ds.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(dias_etapa1, fallas_acumuladas_etapa1,
                                                                                aprox_inicial_ds)

params_ds_mv_etapa_1 = ds.estimar_parametros_por_maxima_verosimilitud_fallas_acumuladas_al_dia(dias_etapa1,
                                                                                               fallas_acumuladas_etapa1,
                                                                                               params_ds_lsq_etapa_1,
                                                                                               metodo_resolucion='krylov')

# De 101 al final

# TO-DO: probar con la forma general en lugar de la probabilidad condicional

aprox_inicial_go = (1, 0.001)
dias_etapa2 = dias[100:]
fallas_por_dia_etapa2 = fallas_por_dia[100:]
fallas_acumuladas_etapa2 = fallas_acumuladas[100:]

params_go_lsq_etapa_2 = go.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(dias_etapa2, fallas_acumuladas_etapa2,
                                                                                aprox_inicial_go)

params_go_mv_etapa_2 = go.estimar_parametros_por_maxima_verosimilitud_fallas_por_dia(dias_etapa2,
                                                                                     fallas_por_dia_etapa2,
                                                                                     params_go_lsq_etapa_2,
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


# Datos reales
ax.plot(dias, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--',
        label='Datos reales (Mixed Waterfall-Agile)')

# Plot Etapa 1
ax.plot(dias_etapa1, ds.calcular_numero_medio_de_fallas(dias_etapa1, params_ds_lsq_etapa_1[0], params_ds_lsq_etapa_1[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ - Etapa 1: a=%.5f, b=%.5f'
                                                           % tuple(params_ds_lsq_etapa_1))
if params_ds_mv_etapa_1 is not None:
    ax.plot(dias_etapa1, ds.calcular_numero_medio_de_fallas(dias_etapa1, params_ds_mv_etapa_1[0], params_ds_mv_etapa_1[1]),
            linewidth=1, color='#58b368', linestyle='-', label='MV - Etapa 1: a=%.5f, b=%.5f'
                                                               % tuple(params_ds_mv_etapa_1))

# Plot Etapa 2
ax.plot(dias_etapa2, go.calcular_numero_medio_de_fallas(dias_etapa2, params_go_lsq_etapa_2[0], params_go_lsq_etapa_2[1]),
        linewidth=1, color='#ca3e47', linestyle='-', label='LSQ - Etapa 2: a=%.5f, b=%.5f'
                                                           % tuple(params_go_lsq_etapa_2))
if params_go_mv_etapa_2 is not None:
    ax.plot(dias_etapa2, go.calcular_numero_medio_de_fallas(dias_etapa2, params_go_mv_etapa_2[0], params_go_mv_etapa_2[1]),
            linewidth=1, color='#58b368', linestyle='-', label='MV - Etapa 2: a=%.5f, b=%.5f'
                                                               % tuple(params_go_mv_etapa_2))

ax.legend()

ax.plot()
plt.show()
