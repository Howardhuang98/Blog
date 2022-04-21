#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1414.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/21 14:58  
------------      
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        cnt = 1
        while True:
            a = 1
            b = 1
            while not a <= k < b:
                a, b = b, a + b
            k = k - a
            if k == 0:
                return cnt
            else:
                cnt += 1

if __name__ == '__main__':
    s = Solution()
    print(s.findMinFibonacciNumbers(19))

