#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   942.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/9 20:48  
------------      
"""
import collections
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        ans = []
        for char in s:
            if char == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans

