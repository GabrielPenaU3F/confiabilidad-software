from data.agile1_data import AgileN1Data
from data.agile2_data import AgileN2Data
from data.agile3_data import AgileN3Data
from data.agile4_data import AgileN4Data
from data.mixed_waterfall_agile_data import MixedWaterfallAgileData
from data.ntds_data import NTDSData
from src.exceptions.exceptions import InvalidArgumentException


class DataRepository:

    data = {
      'ntds': NTDSData(),
      'agile-n1': AgileN1Data(),
      'mixed-waterfall-agile': MixedWaterfallAgileData(),
      'agile-n2': AgileN2Data(),
      'agile-n3': AgileN3Data(),
      'agile-n4': AgileN4Data(),
    }

    @classmethod
    def provide_project_data(cls, project_name):
        if cls.data.keys().__contains__(project_name):
            return cls.data.get(project_name)
        else:
            raise InvalidArgumentException('The requested project is not on the repository')
