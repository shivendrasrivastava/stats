__author__ = "Shiven"

import math

class StandardDeviation(object):

    def __init__(self):pass

    def cal_deviation(self):
        arr_int = list(map(int, input().split()))
        mean = sum(arr_int)/len(arr_int)
        dist_from_mean = 0
        for x in range(len(arr_int)):
            dist_from_mean += (abs(arr_int[x] - mean))**2
        value = math.sqrt(dist_from_mean/len(arr_int))
        rounded_value = round(value, 1)
        print(rounded_value)
        return rounded_value
