# Converting array from one data type to the other
import numpy as np
def solution(array):
    a1 = np.array(array)
    a2 = a1.astype(float)
    return a2
