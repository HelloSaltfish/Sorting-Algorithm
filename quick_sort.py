# -*- encoding: utf-8 -*-
"""
@File    : 22 快速排序.py
@Time    : 2021/5/21 11:22
@Author  : saltfish
@e-mail : 178826392@qq.com
@phone : 17681861018
"""


def partition(l1, left, right):
    temp = l1[left]
    while left < right:
        while left < right and l1[right] >= temp:
            right -= 1
        l1[left] = l1[right]
        while left < right and l1[left] <= temp:
            left += 1
        l1[right] = l1[left]
    l1[left] = temp
    return left


def quick_sort(l1, left, right):
    if left < right:
        mid = partition(l1, left, right)
        quick_sort(l1, left, mid-1)
        quick_sort(l1, mid + 1, right)


import random

l1 = [random.randint(1, 100) for x in range(10)]
print(l1)

quick_sort(l1, 0, len(l1) - 1)
print(l1)
