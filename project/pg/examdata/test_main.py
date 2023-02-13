from pg.examdata.test_data import *


def data(expID: int):
    list = [test0(),
            test1(),
            ]
    options = list[expID]
    return options

