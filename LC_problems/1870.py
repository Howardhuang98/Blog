#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1870.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/5 19:16  
------------      
"""
import math
from typing import List
from decimal import Decimal


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        elif len(dist) > hour > len(dist) - 1:

            return max(math.ceil(round(dist[-1]/ (hour - int(hour)),3)), max(dist))
        else:
            l = 1
            r = max(dist)
            while l < r:
                mid = (l + r) // 2
                pre = 0
                t = 0
                for distance in dist:
                    t = math.ceil(pre) + (distance / mid)
                    pre = t
                if t > hour:
                    l = mid+1
                else:
                    r = mid
            return r


if __name__ == '__main__':
    s = Solution()
    print(s.minSpeedOnTime([5,3,4,6,2,2,7],10.92))
