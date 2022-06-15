"""
Implementation of a merge sort
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid_point = len(array) // 2
    left = array[:mid_point]
    right = array[mid_point:]
    right = merge_sort(right)
    left = merge_sort(left)
    return merge(left, right)


def merge(arr1, arr2):
    lst = []
    i = 0
    j = 0
    while i < len(arr2) and j < len(arr1):
        if arr2[i] < arr1[j]:
            lst.append(arr2[i])
            i += 1
        else:
            lst.append(arr1[j])
            j += 1
    while i < len(arr2):
        lst.append(arr2[i])
        i += 1
    while j < len(arr1):
        lst.append(arr1[j])
        j += 1
    return lst
