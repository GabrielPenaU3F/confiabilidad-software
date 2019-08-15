from data.data import AgileN1Data, NTDSData, MixedWaterfallAgileData


class DataRepository:

    data = {
      'ntds': NTDSData(),
      'agile-n1': AgileN1Data(),
      'mixed-waterfall-agile': MixedWaterfallAgileData()
    }

    @classmethod
    def provide_observed_data_from_project(cls, project_name):
        return cls.data.get(project_name)