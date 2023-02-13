import math


def Lineindex(argsx, argsy):
    x2sum = 0
    xsum = 0
    xysum = 0
    ysum = 0
    N = len(argsx)
    j = 0
    for i in argsx:
        x2sum += i**2
        xsum += i
        xysum += (i*argsy[j])
        j += 1
    for k in argsy:
        ysum += k
    a = (x2sum*ysum - xsum*xysum)/(N*x2sum - xsum**2)
    b = (N*xysum - xsum*ysum)/(N*x2sum - xsum**2)
    return [a, b]

def Linedata(argsx,a,b):
    argsy = []
    for i in argsx:
        j = a + b*i
        argsy.append(j)
    return argsy