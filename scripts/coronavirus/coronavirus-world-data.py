from src.data.data_repository import DataRepository
from src.domain.fitters.model_fitter import ModelFitter

DataRepository.load_project_data_from_file(path="../../../test_resource_files/formated_coronavirus_data.ods")

fitter = ModelFitter()
ds_fit = fitter.fit('delayed-s-shaped', 'corona-1', mts=False)
bc_fit = fitter.fit('barraza-contagion', 'corona-1', mts=False)

ds_fit.show_results()
bc_fit.show_results()
