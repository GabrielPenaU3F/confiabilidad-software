from abc import ABC, abstractmethod
from matplotlib import pyplot as plt


class PlotStrategy(ABC):

    @abstractmethod
    def graficar(self, nombre_proyecto, params_mc, params_mv, datos):
        pass

    def formatear_grafica(self, axes):
        axes.set_xlabel('Tiempo (días)')
        axes.set_ylabel('Número de fallas')
        axes.set_xlim(left=0, auto=True)
        axes.set_ylim(bottom=-2, top=2, auto=True)
        axes.patch.set_facecolor("#ffffff")
        axes.patch.set_edgecolor('black')
        axes.patch.set_linewidth('1')
        axes.set_facecolor("#ffffff")
        axes.grid(color='black', linestyle='--', linewidth=0.5)
        axes.legend()
        axes.plot()
        plt.show()
