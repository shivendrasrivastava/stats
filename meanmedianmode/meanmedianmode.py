__author__ = "Shiven"

import collections
import operator


class MeanMedianMode(object):

    def __init__(self):pass

    def calculate_mmm(self):
        #Mean calculation
        arr_int = input().split()
        arr_int = list(map(int, arr_int))
        mean = sum(arr_int)/len(arr_int)
        print(str(mean))
        #Median calculation
        arr_int_sort = sorted(arr_int)
        length = len(arr_int_sort)
        half = int(length/2)
        half_1 = int(half - 1)
        median = (arr_int_sort[half] + arr_int_sort[half-1])/2
        print(str(median))
        #Mode calculation
        occ = dict()
        for x in range(len(arr_int_sort)):
            count = arr_int_sort.count(arr_int_sort[x])
            occ[arr_int_sort[x]] = count
        occ = collections.OrderedDict(sorted(occ.items()))
        print(str(max(occ.items(), key=operator.itemgetter(1))[0]))


if __name__ == "__main__":
    mmm_obj = MeanMedianMode()
    mmm_obj.calculate_mmm()
