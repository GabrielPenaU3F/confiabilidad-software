from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos
from src.goel_okumoto.estimador_goel_okumoto import EstimadorGoelOkumoto

datos = RepositorioDatos.proveer_datos_observados_proyecto_NTDS()
x = datos.get_tiempos_de_falla()
y = datos.get_fallas_acumuladas()

go = EstimadorGoelOkumoto()
params_go = go.ajustar_numero_medio_de_fallas_por_minimos_cuadrados(x, y)

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

ax.plot(x, y, linewidth=1, color='#263859', linestyle='--')
ax.plot(x, go.calcular_numero_medio_de_fallas(x), linewidth=1, color='#ca3e47', linestyle='-')

ax.plot()
plt.show()
