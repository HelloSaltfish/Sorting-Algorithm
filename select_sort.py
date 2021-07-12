# -*- encoding: utf-8 -*-
"""
@File    : 22 选择排序.py
@Time    : 2021/5/20 16:36
@Author  : saltfish
@e-mail : 178826392@qq.com
@phone : 17681861018
"""
import random

l1 = [random.randint(1, 100) for x in range(10)]
print(l1)
for i in range(len(l1)-1):
    min_index = i
    for j in range(i + 1, len(l1)):
        if l1[j] < l1[min_index]:
            min_index = j
    if min_index != i:
      l1[i], l1[min_index] = l1[min_index], l1[i]
print(l1)
