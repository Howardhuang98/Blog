#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   980.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/21 21:30  
------------      
"""
from collections import Counter
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        num_place = 0
        start = (0, 0)
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    num_place += 1

        def dfs(location, walked):


            if grid[location[0]][location[1]] == 2:
                if len(walked) == num_place + 1:
                    results.append(walked + [location])
                    return True
                else:
                    return
            # 可能的方向
            x, y = location
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < height and 0 <= ny < width:
                    if grid[nx][ny] != -1 and (nx, ny) not in walked:
                        dfs((nx, ny), walked + [location])


            return

        results = []
        dfs(start, [])
        print(results)

        return len(results)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    print(s.uniquePathsIII([[1, 0], [2, 0]]))
