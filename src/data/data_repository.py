from data.agile1_data import AgileN1Data
from data.mixed_waterfall_agile_data import MixedWaterfallAgileData
from data.ntds_data import NTDSData
from src.exceptions.exceptions import InvalidArgumentException


class DataRepository:

    data = {
      'ntds': NTDSData(),
      'agile-n1': AgileN1Data(),
      'mixed-waterfall-agile': MixedWaterfallAgileData()
    }

    @classmethod
    def provide_project_data(cls, project_name):
        if cls.data.keys().__contains__(project_name):
            return cls.data.get(project_name)
        else:
            raise InvalidArgumentException('The requested project is not on the repository')
