# -*- coding: utf-8 -*-
import random

test_list_1 = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]
test_list_2 = [8, 1, 2, 100, 12303479849857341718340192371, 3084193741082937, 3084193741082938, 111, 200]

# Quick sort: pivot ngẫu nhiên
def quick_sort(arr):
    if (len(arr) < 2): return arr
    pivot = random.choice(arr)
    left_arr = []
    right_arr = []
    result_arr = []
    for val in arr:
        if val < pivot:
            left_arr.append(val)
        elif val > pivot:
            right_arr.append(val)
        else:
            result_arr.append(val)
    return quick_sort(left_arr) + result_arr + quick_sort(right_arr)

print(quick_sort(test_list_2))