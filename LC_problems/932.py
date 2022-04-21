#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   932.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/21 16:22  
------------      
"""
from typing import List


class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}

        def f(N):
            if N not in memo:
                odds = f((N+1) // 2)
                evens = f(N // 2)
                memo[N] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[N]

        f(N)
        return memo[N]


if __name__ == '__main__':
    s = Solution()
    s.beautifulArray(10)
