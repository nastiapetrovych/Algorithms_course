"""
The bubble sort
"""


def bubble_sort(array):
    for _ in range(len(array)):
        for index in range(len(array) - 1):
            element = array[index + 1]
            if array[index] > element:
                array[index + 1] = array[index]
                array[index] = element
    return array
