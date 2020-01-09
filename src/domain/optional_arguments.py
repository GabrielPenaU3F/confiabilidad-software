import numpy as np

from src.exceptions.exceptions import InvalidArgumentException


class OptionalArguments:

    def __init__(self, **kwargs):
        self.initial_sample = self.determine_initial_sample(kwargs.get('initial_sample'))
        self.end_sample = self.determine_end_sample(kwargs.get('end_sample'))
        self.lsq_only = self.determine_lsq_only(kwargs.get('lsq_only'))
        self.t0 = self.determine_t0(kwargs.get('t0'))
        self.mts_flag = self.determine_mts_flag(kwargs.get('mts'))
        self.initial_approx = self.determine_initial_approx(kwargs.get('initial_approx'))

    def get_initial_sample(self):
        return self.initial_sample

    def get_end_sample(self):
        return self.end_sample

    def get_lsq_only(self):
        return self.lsq_only

    def get_t0(self):
        return self.t0

    def get_mts_flag(self):
        return self.mts_flag

    def get_initial_approx(self):
        return self.initial_approx

    def determine_t0(self, t0):
        if t0 is not None:
            try:
                if float(t0) >= 0:
                    return t0
                else:
                    raise ValueError
            except (ValueError, TypeError):
                raise InvalidArgumentException('Initial condition t0 must be a positive number')
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
                else:
                    raise ValueError
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
            initial_approx = np.array(initial_approx)
            if initial_approx.size > 1:
                [float(approx) for approx in initial_approx]
                return initial_approx
            else:
                return float(initial_approx)
        except (ValueError, TypeError):
            raise InvalidArgumentException('Initial approximation must be a real tuple or array')

    def determine_initial_sample(self, initial_sample):
        if initial_sample is not None:
            try:
                if (int(initial_sample) == initial_sample) and (initial_sample >= 0):
                    return initial_sample
                else:
                    raise ValueError
            except (ValueError, TypeError):
                raise InvalidArgumentException('The initial sample must be a positive integer or zero')
        else:
            return 0

    def set_initial_approx(self, initial_approx):
        self.initial_approx = initial_approx
