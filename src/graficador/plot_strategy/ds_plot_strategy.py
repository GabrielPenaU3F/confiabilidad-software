from src.graficador.plot_strategy.plot_strategy import PlotStrategy
from src.modelos.delayed_s_shaped.estimador_delayed_s_shaped import EstimadorDelayedSShaped
from matplotlib import pyplot as plt


class DSPlotStrategy(PlotStrategy):

    def graficar(self, nombre_proyecto, params_mc, params_mv, datos):
        datos_x = datos.get_datos()
        fallas_acumuladas = datos.get_fallas_acumuladas()
        ds = EstimadorDelayedSShaped()

        fig, ax = plt.subplots()
        ax.plot(datos_x, fallas_acumuladas, linewidth=1, color='#263859', linestyle='--',
                label='Datos reales (' + nombre_proyecto + ')')
        ax.plot(datos_x, ds.calcular_numero_medio_de_fallas(datos_x, params_mc[0], params_mc[1]),
                linewidth=1, color='#ca3e47', linestyle='-', label='Mínimos cuadrados')
        ax.plot(datos_x, ds.calcular_numero_medio_de_fallas(datos_x, params_mv[0], params_mv[1]),
                linewidth=1, color='#58b368', linestyle='-', label='Máxima verosimilitud (Tiempo hasta la falla)')
        self.formatear_grafica(ax)
