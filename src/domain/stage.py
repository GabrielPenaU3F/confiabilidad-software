class Stage:

    def __init__(self, initial_t, end_t, model):
        self.initial_t = initial_t
        self.end_t = end_t
        self.model = model

    def get_initial_t(self):
        return self.initial_t

    def get_end_t(self):
        return self.end_t

    def get_model(self):
        return self.model

    def be_fitted(self, lsq_params, ml_params):
        return FittedStage(self.initial_t, self.end_t, self.model, lsq_params, ml_params)


class FittedStage(Stage):

    def __init__(self, initial_t, end_t, model, lsq_params, ml_params):
        super().__init__(initial_t, end_t, model)
        self.lsq_params = lsq_params
        self.ml_params = ml_params

    def get_lsq_params(self):
        return self.lsq_params

    def get_ml_params(self):
        return self.ml_params

