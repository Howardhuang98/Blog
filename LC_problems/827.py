#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   827.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/29 21:43  
------------      
"""
import collections
import itertools
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        land = []
        for i in range(height):
            for j in range(width):
                q = collections.deque()
                if grid[i][j] == 1:
                    q.append([i, j])
                    grid[i][j] = 0
                    island = [[i, j]]
                    while q:
                        x, y = q.popleft()
                        for new_x, new_y in [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]:
                            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] == 1:
                                q.append([new_x, new_y])
                                grid[new_x][new_y] = 0
                                island.append([new_x, new_y])
                    land.append(island)
        ans = 0
        memo = {}
        for n in range(len(land)):
            area = len(land[n])
            ans = max(ans, area)
            for x, y in land[n]:
                grid[x][y] = n + 1
                memo[n + 1] = area

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    neibor = []
                    for new_i, new_j in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
                        if 0 <= new_i < height and 0 <= new_j < width and grid[new_i][new_j] != 0:
                            n_island = grid[new_i][new_j]
                            if n_island not in neibor:
                                neibor.append(n_island)

                    ans = max(sum(memo[n] for n in neibor) + 1, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestIsland([[0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 1, 0, 0],
                           [0, 1, 0, 0, 1, 0, 0],
                           [1, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 0, 0],
                           [0, 1, 1, 1, 1, 0, 0]]))
