#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1716.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/23 21:44  
------------      
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        money =  0
        n_weeks = n//7
        remains = n%7
        if n_weeks != 0:
            money += (56+(n_weeks-1)*7)*n_weeks/2
        if remains != 0:
            for i in range(n_weeks,n+remains):
                money+=i
        return money

if __name__ == '__main__':
    s= Solution()
    print(s.totalMoney(7))