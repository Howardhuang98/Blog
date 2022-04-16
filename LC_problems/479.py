#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   479.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/16 13:27  
------------      
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):  # 枚举回文数的左半部分
            p, x = left, left
            while x:
                p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数 p
                x //= 10
            x = upper

            while x * x >= p:
                if p % x == 0:  # x 是 p 的因子
                    return p % 1337
                x -= 1



if __name__ == '__main__':
    s = Solution()
    print(s.largestPalindrome(2))
