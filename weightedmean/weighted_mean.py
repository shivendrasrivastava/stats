__author__ = "Shiven"

def cal_wghtd_mean():
    arr_int = list(map(int, input().split()))
    wght_int = list(map(int, input().split()))
    wght_sum = sum(wght_int)
    wght_prod = [a*b for a, b in zip(arr_int, wght_int)]
    rounded_value = round((sum(wght_prod)/wght_sum),4)
    print(rounded_value)
    return rounded_value
