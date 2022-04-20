#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6070.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/17 10:32  
------------      
"""
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def cal(x, y):
            up, down, left, right = 1, 1, 1, 1
            for i in range(len(grid)):
                if i < x:
                    up = up * grid[i][y]
                if i > x:
                    down = down * grid[i][y]
            for j in range(len(grid[0])):
                if j < y:
                    left = left * grid[x][j]

                if j > y:
                    right = right * grid[x][j]
                    ans = [up * grid[x][y] * left,
                           up * grid[x][y] * right,
                           down * grid[x][y] * left,
                           down * grid[x][y] * right]
            res = []
            for i, a in enumerate(ans):
                res.append(len(str(a)) - len(str(a).rstrip("0")))
            print(res)
            return max(res)

        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                ans = max(cal(x, y), ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxTrailingZeros(
        [[824, 709, 193, 413, 701, 836, 727],
         [135, 844, 599, 211, 140, 933, 205],
         [329, 68, 285, 282, 301, 387, 231],
         [293, 210, 478, 352, 946, 902, 137],
         [806, 900, 290, 636, 589, 522, 611],
         [450, 568, 990, 592, 992, 128, 92],
         [780, 653, 795, 457, 980, 942, 927],
         [849, 901, 604, 906, 912, 866, 688]]))

    print(s.maxTrailingZeros(
        [[4, 3, 2], [7, 6, 1], [8, 8, 8]]))
