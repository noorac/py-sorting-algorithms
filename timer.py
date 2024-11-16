from decimal import Decimal, getcontext
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        starttime = time()
        funcreturn = func(*args, **kwargs)
        endtime = time()
        getcontext().prec = 3
        elapsedtime = Decimal(endtime) - Decimal(starttime)
        return funcreturn, elapsedtime

    return wrapper
