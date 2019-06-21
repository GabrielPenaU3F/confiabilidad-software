from matplotlib import pyplot as plt

from datos.repositorio_datos import RepositorioDatos

datos = RepositorioDatos.proveer_datos_observados_proyecto_NTDS()
x = datos.get_tiempos_de_falla()
y = datos.get_fallas_acumuladas()

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
ax.plot()
plt.show()
