# -*- coding: utf-8 -*-
import random

# Increasing sort

# Test case
test_case = [
    [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5],
    [8, 1, 2, 100, 12303479849857341718340192371, 3084193741082937, 3084193741082938, 111, 200],
    [10097, 32533, 76520, 13586, 34673, 54876, 80959, 9117,  39292, 74945],
]

# Swap
def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr

# Thuật toán đơn giản (Độ phức tạp thuật toán - O(n^2)):
# Insertion sort: O(n^2)
def insertionSort(arr):
    for index, value in enumerate(arr):
        last = value
        j = index
        while j > 0 and arr[j-1] > last:
            arr[j] = arr[j-1]
            arr[j-1] = last
            j -= 1
    return arr

# Selection sort: O(n^2)
def selectionSort(arr):
    for index in range(len(arr)):
        min = index
        for index2 in range(index + 1, len(arr)):
            if arr[index2] < arr[min]: min = index2
        arr = swap(arr, index, min)
    return arr

# Bubble sort: O(n^2)
def bubbleSort(arr):
    for index in range(len(arr) - 1, 0, -1):
        for index2 in range(1, index + 1):
            if arr[index2 - 1] > arr[index2]: arr = swap(arr, index2 - 1, index2)
    return arr

# Thuật toán hiệu quả (Độ phức tạp thuật toán - O(nlogn)):
# Merge sort: O(nlogn)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
    return arr

# Quick sort: O(n^2) (random pivot)
def quickSort(arr):
    if (len(arr) < 2): return arr
    pivot = random.choice(arr) # random pivot
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
    return quickSort(left_arr) + result_arr + quickSort(right_arr)

# Heap sort: O(nlogn)

# Thuật toán đăc biệt (Độ phức tạp thuật toán - O(n)):
    # Sắp xếp đếm (Counting Sort)
    # Sắp xếp phân cụm (Bucket Sort)
    # Sắp xếp cơ số (Radix Sort)
# Xử lý các tập dữ liệu lớn:
    # Sắp xếp ngoài (External sort)

# Execution
print(quickSort(test_case[0]))
