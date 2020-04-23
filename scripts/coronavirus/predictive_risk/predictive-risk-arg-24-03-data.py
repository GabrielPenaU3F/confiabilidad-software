import numpy as np
from colorama import Fore

from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

from src.domain.models.barraza_contagion.barraza_contagion_estimator import BarrazaContagionEstimator

DataRepository.load_project_data_from_file(path="../../../test_resource_files/covid_data_by_date/arg-24-03.ods")

fitter = ModelFitter()
bc_fit_10 = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False, end_sample=10)
bc_fit_12 = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False, end_sample=12)
bc_fit_15 = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False, end_sample=15)
bc_fit_18 = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False, end_sample=18)
bc_fit_20 = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False, end_sample=20)
bc_fit = fitter.fit('barraza-contagion', 'corona1-arg-24-03', mts=False)



fig, axes = plt.subplots()

data = DataRepository.provide_project_data('corona1-arg-24-03')
tiempos = data.get_times()
bc = BarrazaContagionEstimator()

print(Fore.YELLOW + 'PRR - 10 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_10.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 12 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_12.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 15 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_15.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 18 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_18.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - 20 datos:')
print(Fore.LIGHTRED_EX + (bc_fit_20.get_prr_lsq().__str__()))

print(Fore.YELLOW + 'PRR - Full dataset:')
print(Fore.LIGHTRED_EX + (bc_fit.get_prr_lsq().__str__()))

axes.plot(data.get_times(), data.get_cumulative_failures(), linewidth=2, color='blue',
          label='Datos reales en Argentina - 4/3/20 al 24/3/20')
axes.plot(tiempos, bc.calculate_mean(tiempos, *bc_fit.get_lsq_parameters()), linewidth=1, color='red',
          label='Ajuste con el dataset completo')

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