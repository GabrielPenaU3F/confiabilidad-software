class Stage:

    def __init__(self, initial_t, end_t, model):
        self.initial_t = initial_t
        self.end_t = end_t
        self.model = model
        self.lsq_params = None
        self.ml_params = None

    def get_initial_t(self):
        return self.initial_t

    def get_end_t(self):
        return self.end_t

    def get_model(self):
        return self.model

    def set_lsq_params(self, lsq_params):
        self.lsq_params = lsq_params

    def set_ml_params(self, ml_params):
        self.ml_params = ml_params

    def get_lsq_params(self):
        return self.lsq_params

    def get_ml_params(self):
        return self.ml_params
