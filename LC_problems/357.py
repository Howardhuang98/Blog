#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   357.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/11 15:52  
------------      
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(1))
    print(s.countNumbersWithUniqueDigits(2))
    print(s.countNumbersWithUniqueDigits(3))