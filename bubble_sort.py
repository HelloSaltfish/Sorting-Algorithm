# -*- encoding: utf-8 -*-
"""
@File    : 21 冒泡排序.py
@Time    : 2021/5/12 12:08
@Author  : saltfish
@e-mail : 178826392@qq.com
@phone : 17681861018
"""

import random

l1 = [random.randint(1, 100) for x in range(10)]
print(l1)
for i in range(len(l1)-1):
    for j in range(len(l1)-1-i):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1] = l1[j+1],l1[j]



print(l1)
