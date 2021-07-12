# -*- encoding: utf-8 -*-
"""
@File    : 22  插入排序.py
@Time    : 2021/5/12 12:16
@Author  : saltfish
@e-mail : 178826392@qq.com
@phone : 17681861018
"""

import random

l1 = [random.randint(1, 100) for x in range(10)]
print(l1)
li_len = len(l1)
for i in range(1, li_len):
    temp = l1[i]
    if l1[i] < l1[i - 1]:
        j = i - 1
        while j >= 0 and l1[j] > temp:
            l1[j + 1] = l1[j]
            j -= 1
        l1[j + 1] = temp

print(l1)
