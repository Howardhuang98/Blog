#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   蔚来3.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/23 21:10  
------------      
"""
from functools import lru_cache


def solu(N: int, sequence: str):
    @lru_cache()
    def dp(start: int, end):
        if end - start < 3:
            return set()
        return set([sequence[s:s + 3] for s in range(start, end, 3)])

    for i in range(N):
        margin = i
        while margin % 3 != 0:
            margin -= 1
        if N-margin<3:
            ans = set()
        else:
            ans = {sequence[margin:i] + sequence[i + 1:min(margin + 4, N)]}
        ans |= dp(0, margin)
        ans |= dp(min(N, margin + 4), N)
        print(ans)
        print(len(ans))


if __name__ == '__main__':
    solu(5, "CCCCCC")
