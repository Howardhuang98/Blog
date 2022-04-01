#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   728.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/31 11:55  
------------      
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for x in range(left,right+1):
            flag = True
            n = x
            while n:
                n,d = divmod(n,10)
                if d==0 or n%d:
                    flag = False
            if flag:
                ans.append(x)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.selfDividingNumbers(47,85)