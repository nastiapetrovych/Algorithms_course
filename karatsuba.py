"""
The way how to multiply the big numbers with time complexity O(n)
"""


def karatsuba(first_number, second_number):
    if len(str(first_number)) < 10 or len(str(second_number)) < 10:
        return first_number * second_number
    length = max(len(str(first_number)), len(str(second_number)))
    medium = length // 2
    a = str(first_number)[:medium]
    b = str(first_number)[medium:]
    c = str(second_number)[:medium]
    d = str(second_number)[medium:]
    ac = karatsuba(int(a), int(c))
    bd = karatsuba(int(b), int(d))
    sum_numbers = karatsuba(int(a) + int(b), int(c) + int(d)) - ac - bd
    return ac * (10 ** length) + sum_numbers * (10 * medium) + bd
