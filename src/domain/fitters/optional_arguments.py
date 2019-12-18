import numpy as np

from src.exceptions.exceptions import InvalidArgumentException


class OptionalArguments:

    def __init__(self, **kwargs):
        self.end_sample = self.determine_end_sample(kwargs.get('end_sample'))
        self.lsq_only = self.determine_lsq_only(kwargs.get('lsq_only'))
        self.x0 = self.determine_x0(kwargs.get('x0'))
        self.mts_flag = self.determine_mts_flag(kwargs.get('mts'))
        self.initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

    def get_end_sample(self):
        return self.end_sample

    def get_lsq_only(self):
        return self.lsq_only

    def get_x0(self):
        return self.x0

    def get_mts_flag(self):
        return self.mts_flag

    def get_initial_approx(self):
        return self.initial_approx

    def determine_x0(self, x0):
        if x0 is not None:
            try:
                if float(x0) > 0:
                    return x0
            except (ValueError, TypeError):
                raise InvalidArgumentException('Initial condition x0 must be a positive number')
        else:
            return 0

    def determine_mts_flag(self, mts_flag):
        #  MTTF and MTTF calculations are done by default, so True is the default behaviour
        if mts_flag is not False:
            return True
        else:
            return mts_flag

    def determine_end_sample(self, end_sample):
        if end_sample is not None:
            try:
                if (int(end_sample) == end_sample) and (end_sample > 0):
                    return end_sample
            except (ValueError, TypeError):
                raise InvalidArgumentException('The end sample must be a positive integer')
        else:
            return 0

    def determine_lsq_only(self, lsq_only):
        if lsq_only is not True:
            return False
        else:
            return lsq_only

    def determine_initial_approx(self, initial_approx):
        if initial_approx is None:
            return None
        try:
            np.array(initial_approx)
            return initial_approx
        except (ValueError, TypeError):
            raise InvalidArgumentException('Initial approximation must be a real tuple or array')
