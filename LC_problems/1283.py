#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1283.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/26 21:55  
------------      
"""
import math
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        n = 10**(math.ceil(intLength/2)-1)
        result = []
        for q in queries:
            base = n
            base = base+q-1
            if intLength % 2 == 0:
                res_str = str(base)+str(base)[::-1]
                result.append(int(res_str))
            else:
                res_str = str(base)+ str(base)[-2::-1]
                result.append(int(res_str))
        return result
if __name__ == '__main__':
    s =  Solution()
    print(s.kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3))
