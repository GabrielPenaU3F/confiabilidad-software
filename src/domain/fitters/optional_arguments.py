import numpy as np

from src.exceptions.exceptions import InvalidInitialConditionException


class OptionalArguments:

    def __init__(self, x0, mts_flag):
        self.x0 = self.determine_x0(x0)
        self.mts_flag = self.determine_mts_flag(mts_flag)

    def determine_x0(self, x0):
        if x0 is not None:
            try:
                if float(x0) > 0:
                    return x0
            except (ValueError, TypeError):
                raise InvalidInitialConditionException('Initial condition x0 must be a positive number')
        else:
            return 0

    def determine_mts_flag(self, mts_flag):
        #  MTTF and MTTF calculations are done by default, so True is the default behaviour
        if mts_flag is not False:
            return True
        else:
            return mts_flag

    def get_mts_flag(self):
        return self.mts_flag

    def get_x0(self):
        return self.x0
