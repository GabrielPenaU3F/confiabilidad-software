from src.domain.data import AgileN1Data, NTDSData, MixedWaterfallAgileData


class DataRepository:

    data = {
      'ntds': NTDSData(),
      'agile-n1': AgileN1Data(),
      'mixed-waterfall-agile': MixedWaterfallAgileData()
    }

    @classmethod
    def provide_project_data(cls, project_name):
        return cls.data.get(project_name)
