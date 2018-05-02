from random import uniform, randrange
from keras.losses import *
from keras.optimizers import *


class BaseConfig:
    def __init__(self):
        self.EPOCHS = 200
        self.BATCH_SIZE = 128

        self.HOUSE_ID = 5

        # 0 - 23
        self.HOUR_TO_PREDICT = 17

        self.HOURS_PAST = 24
        self.WEEKS = 5

        self.HIDDEN_LAYERS = [55]

        self.BIAS = True
        self.ACTIVATION_FUNCTION = 'relu'
        self.LOSS = mean_squared_error
        self.OPTIMIZER = Adamax()
        self.SCALE_VALUES = False

        self.TRAINING_CUT = 0.7
        self.DATA_SLICE = 1
        self.GRAPH_CUT = 1

        # -- Features --
        # Same hours in past days past weeks
        # X hours past
        # Day of week
        # Specific features from csv
        self.FEATURES = [1, 0, 0, 0]

    def dump(self):
        result = {}
        for sk in vars(self):
            result[sk] = self.__getattribute__(sk)
        return result


class MultiConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        # self.CRITICAL_START = [13, 17]
        # self.CRITICAL_END = [19, 24]

        # self.CRITICAL_START_WE = [8, 14]
        # self.CRITICAL_END_WE = [18, 24]

        for lvk in vars(self):
            lv = self.__getattribute__(lvk)
            if isinstance(lv, list):
                if len(lv) == 3 and isinstance(lv[2], int) and lv[2] >= 0:
                    # we assume last value is precision limit
                    prec = lv[2]
                else:
                    prec = 2

                if isinstance(lv[0], int) and isinstance(lv[1], int):
                    lv = randrange(lv[0], lv[1] + 1)
                elif isinstance(lv[0], float) or isinstance(lv[1], float):
                    lv = round(uniform(lv[0], lv[1]), prec)

                self.__setattr__(lvk, lv)


class SingleConfig(BaseConfig):
    def __init__(self):
        super().__init__()