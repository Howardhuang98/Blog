#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1613.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/30 19:50  
------------      
"""
from typing import List


class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        x1, y1, d1 = square1
        x2, y2, d2 = square2
        center1 = [x1 + d1 / 2, y1 + d1 / 2]
        center2 = [x2 + d2 / 2, y2 + d2 / 2]
        if center1 == center2:
            d = max(square1[2], square2[2])
            return [center1[0], min(y1, y2), center1[0], max(y1 + d1, y2 + d2)]
        elif center1[0] == center2[0]:
            return [center1[0], min(y1, y2), center1[0], max(y1 + d1, y2 + d2)]
        elif center1[1] == center2[1]:
            return [min(x1, x2), center1[1], max(x1 + d1, x2 + d2), center1[1]]
        else:
            k = (center1[1] - center2[1]) / (center1[0] - center2[0])
            b = center1[1] - k * center1[0]
            return [min(x1, x2), k * min(x1, x2) + b, max(x1 + d1, x2 + d2), k * max(x1 + d1, x2 + d2) + b]


if __name__ == '__main__':
    s = Solution()
    print(s.cutSquares([249,-199,5],[-1,136,76]))
    a = {}
    if not a[1]:
        print("a")
