from datos.datos import AgileN1Data, NTDSData, MixedWaterfallAgileData


class DataRepository:

    datos = {
      'ntds': NTDSData(),
      'agile-n1': AgileN1Data(),
      'mixed-waterfall-agile': MixedWaterfallAgileData()
    }

    @classmethod
    def provide_observed_data_from_project(cls, project_name):
        return cls.datos.get(project_name)
