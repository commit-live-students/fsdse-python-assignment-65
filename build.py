import numpy as np


def solution(array):
    if type(array) == list:
        y = array
        y = [ float(e1) for e1 in y]
        return np.array(y)
    x = array.tolist()
    x = [ float(e) for e in x]
    return np.array(x)


solution([1,2,3,4])
