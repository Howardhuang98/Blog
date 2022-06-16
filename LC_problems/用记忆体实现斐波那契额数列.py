#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   用记忆体实现斐波那契额数列.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/21 11:08  
------------      
"""
import time
from functools import lru_cache

memo = {}


def original_f(x):
    if x < 1:
        return 0
    if x == 1:
        return 1
    else:
        res = original_f(x - 1) + original_f(x - 2)
        return res


def f(x):
    if x in memo:
        return memo[x]
    if x < 1:
        return 0
    if x == 1:
        return 1
    else:
        res = f(x - 1) + f(x - 2)
        memo[x] = res
        return res


@lru_cache()
def f_cache(x):
    if x < 1:
        return 0
    if x == 1:
        return 1
    else:
        res = f(x - 1) + f(x - 2)
        return res


if __name__ == '__main__':
    n = 18
    start = time.time()
    print(f(n))
    print("字典记忆体",time.time() - start)
    start = time.time()
    print(original_f(n))
    print("无优化",time.time() - start)
    start = time.time()
    print(f_cache(n))
    print("内置cache",time.time() - start)

