import numpy as np

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

ttf_fitter = ModelFitter()
ds_fit = ttf_fitter.fit('delayed-s-shaped', 'agile-n3')
log_fit = ttf_fitter.fit('logistic', 'agile-n3', initial_approx=(30, 0.03, 300))
bc_fit = ttf_fitter.fit('barraza-contagion', 'agile-n3')

data = DataRepository.provide_project_data('agile-n3')
real_tbf = data.get_time_between_failures()
x_axis_data = np.linspace(1, len(real_tbf), len(real_tbf))

ds_mtbf = ds_fit.get_all_mtbf()
log_mtbf = log_fit.get_all_mtbf()
bc_mtbf = bc_fit.get_all_mtbf()

fig, axes = plt.subplots()
axes.set_xlabel('Número de falla')
axes.set_ylabel('Tiempo medio entre fallas')
axes.set_xlim(left=0, auto=True)
axes.set_ylim(auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.scatter(x_axis_data, real_tbf, linewidth=1, color='#263859', s=4.0,
          label='Datos reales (Proyecto Ágil #3)')
axes.plot(x_axis_data, ds_mtbf,
          linewidth=1, color='#ca3e47', linestyle='-', label='Delayed S-Shaped')
axes.plot(x_axis_data, log_mtbf,
          linewidth=1, color='#58b368', linestyle='-', label='Logístico')
axes.plot(x_axis_data, bc_mtbf,
          linewidth=1, color='#4a47a3', linestyle='-', label='Contagio')
axes.legend()

plt.show()