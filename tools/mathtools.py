import math
import numpy as np


def Lineindex(argsx, argsy):
    x2sum = np.sum(np.multiply(argsx, argsx))
    xsum = np.sum(argsx)
    xysum = np.sum(np.multiply(argsx, argsy))
    ysum = np.sum(argsy)
    N = len(argsx)
    a = (x2sum * ysum - xsum * xysum) / (N * x2sum - xsum ** 2)
    b = (N * xysum - xsum * ysum) / (N * x2sum - xsum ** 2)
    r = ((xysum/N)-np.average(argsx)*np.average(argsy))/np.sqrt(np.var(argsx)*np.var(argsy))
    return [a, b, r]


def Linedata(argsx, a, b):
    argsy = []
    for i in argsx:
        j = a + b * i
        argsy.append(j)
    return argsy
