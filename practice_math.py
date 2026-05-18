import numpy as np

a = -16
b = -1
h = (b - a) / 9
n_array = [3, 18, 56, 86, 69, 42, 18, 3, 1]


def build_interval(a, h):
    i = 1
    array = [a]
    while i != 10:
        last = array[i - 1]
        current = last + h
        array.append(current)
        last = current
        i += 1
    print(f"{array:.6f}")


build_interval(a, h)
