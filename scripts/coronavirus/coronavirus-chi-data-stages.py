import numpy as np

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

from src.domain.fitters.multistage_fitter import MultistageFitter
from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator

DataRepository.load_project_data_from_file(path="../../test_resource_files/coronavirus-chi.ods")

fitter = ModelFitter()
bc_fit = fitter.fit('barraza-contagion', 'corona1-chi', mts=False, end_sample=28)
bc_fit.show_results()

a, b = bc_fit.get_lsq_parameters()

fig, axes = plt.subplots()

data = DataRepository.provide_project_data('corona1-chi')
bc = BarrazaContagionEstimator()

tiempos_15 = np.linspace(1, len(data.get_times()) + 15, len(data.get_times()) + 15)
tiempos_30 = np.linspace(1, len(data.get_times()) + 30, len(data.get_times()) + 30)
axes.plot(data.get_times(), data.get_cumulative_failures(), linewidth=2, color='blue',
                  label='Datos reales en China - 20/3/20')
axes.plot(tiempos_30, bc.calculate_mean(tiempos_30, a, b), linewidth=1, color='red',
          label='Proyección a 30 días')

axes.set_xlim(left=0, auto=True)
axes.set_ylim(bottom=0, auto=True)
axes.patch.set_facecolor("#ffffff")
axes.patch.set_edgecolor('black')
axes.patch.set_linewidth('1')
axes.set_facecolor("#ffffff")
axes.grid(color='black', linestyle='--', linewidth=0.5)
axes.set_xlabel('Failure')
axes.legend()

plt.show()

multistage_fitter = MultistageFitter()
multistage_fitter.add_stage(0, 28, 'barraza-contagion')
multistage_fitter.add_stage(28, len(data.get_times()), 'goel-okumoto')
ms_fit = multistage_fitter.fit('corona1-chi', lsq_only=True)

ms_fit.show_results()