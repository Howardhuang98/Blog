#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   200.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 15:21  
------------      
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        对每个点都进行搜索，将其沉下去

        """
        h = len(grid)
        w = len(grid[0])

        def dfs(x, y):

            # 沉岛
            grid[x][y] = '0'
            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= new_x < h and 0 <= new_y < w and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)

        ans = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
                else:
                    continue
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
