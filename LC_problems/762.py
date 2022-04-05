#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   762.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/5 11:15  
------------      
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        for x in range(left, right + 1):
            n = sum([int(i) for i in str(bin(x))[2:]])
            flag = True
            if n > 1:
                for a in range(2, n):
                    if n % a == 0:
                        print(n)
                        print(a)
                        flag = False
                        break
            else:
                flag = False
            if flag:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(6, 10))
