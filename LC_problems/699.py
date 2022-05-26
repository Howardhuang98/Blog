#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   699.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/26 17:22  
------------      
"""
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        height = [p[1] for p in positions]
        for i, (left, l) in enumerate(positions):
            if i == 0:
                continue
            else:
                for j in range(i):
                    # left,left+l
                    # positions[j][0],positions[j][0] + positions[j][1]
                    if not left >= positions[j][0] + positions[j][1] and not left + l <= positions[j][0]:
                        height[i] = max(height[i], height[j] + l)
        ans = []
        for i, h in enumerate(height):
            if i == 0:
                ans.append(h)
                continue
            else:
                if h < ans[-1]:
                    ans.append(ans[-1])
                else:
                    ans.append(h)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fallingSquares([[9, 6], [2, 2], [2, 6]]))
