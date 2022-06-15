"""
The insertion sort algorithm implemented on my own
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        current = i - 1
        position = array[i]
        while current >= 0 and array[current] > position:
            array[current + 1] = array[current]
            current -= 1
        array[current + 1] = position
    print(array)
