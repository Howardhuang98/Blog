#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   883.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/26 16:21  
------------      
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        z_area = set()
        x_area = set()
        y_area = set()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                v = grid[x][y]
                print(x, y, v)
                if v>0:
                    z_area.add((x, y))
                    for z in range(v):
                        x_area.add((y, z))
                        y_area.add((x, z))
        #print(z_area, x_area, y_area)
        return len(z_area) + len(x_area) + len(y_area)


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[1, 0], [0, 2]]))
