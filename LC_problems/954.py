#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   954.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/1 11:41  
------------      
"""
import collections
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        if c[0] % 2 != 0:
            return False
        for k in sorted(c, key=abs):
            if c[k] > c[2 * k]:
                return False
            elif c[k]!=0:
                c[2 * k] = c[2 * k] - c[k]
                c[k] = 0
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canReorderDoubled([2, 4, 0, 0, 8, 1]))
