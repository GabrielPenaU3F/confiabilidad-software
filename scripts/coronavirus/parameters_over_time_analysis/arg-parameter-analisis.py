from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter
from matplotlib import pyplot as plt

DataRepository.load_project_data_from_file(path="../../test_resource_files/covid_data_by_date/arg-22-04.ods")

fitter = ModelFitter()

data = DataRepository.provide_project_data('corona1-arg-22-04')

fits = {}
fits[10] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=10)
fits[15] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=15)
fits[20] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=20)
fits[25] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=25)
fits[30] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=30)
fits[35] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=35)
fits[40] = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False, end_sample=35)
fits[len(data.get_data())] = bc_fit = fitter.fit('barraza-contagion', 'corona1-arg-22-04', mts=False)

a_params = []
b_params = []
keys = sorted(fits.keys())
for k in keys:
    params = fits[k].get_lsq_parameters()
    a_params.append(params[0])
    b_params.append(params[1])

fig, axes = plt.subplots(1, 2)

times = keys

axes[0].plot(times, a_params, linewidth=2, color='blue',
                  label='Parametro a en función del tiempo - Datos de Argentina 4/3/20 al 22/4/20')
axes[1].plot(times, b_params, linewidth=2, color='red',
                  label='Parametro b en función del tiempo - Datos de Argentina 4/3/20 al 22/4/20')

for ax in axes:
    ax.set_xlim(left=0, auto=True)
    ax.set_ylim(bottom=0, auto=True)
    ax.patch.set_facecolor("#ffffff")
    ax.patch.set_edgecolor('black')
    ax.patch.set_linewidth('1')
    ax.set_facecolor("#ffffff")
    ax.grid(color='black', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Day')
    ax.legend()

plt.show()