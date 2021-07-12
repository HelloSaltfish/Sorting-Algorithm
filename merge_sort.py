# -*- encoding: utf-8 -*-
"""
@File    : 22 归并排序.py
@Time    : 2021/6/20 10:08
@Author  : saltfish
@e-mail : 178826392@qq.com
@phone : 17681861018
"""


def merge(l1, low, mid, high):
    i = low
    j = mid + 1
    temp = []
    while i <= mid and j <= high:
        if l1[i] < l1[j]:
            temp.append(l1[i])
            i += 1
        else:
            temp.append(l1[j])
            j += 1

    while i <= mid:
        temp.append(l1[i])
        i += 1
    while j <= high:
        temp.append(l1[j])
        j += 1

    l1[low:high + 1] = temp


def merge_sort(l1, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(l1, low, mid)
        merge_sort(l1, mid + 1, high)
        merge(l1, low, mid, high)

import random
l1 = [random.randint(1,100) for _ in range(5)]
print(l1)
merge_sort(l1,0,len(l1)-1)
print(l1)