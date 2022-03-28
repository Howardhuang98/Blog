#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   695.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 15:28  
------------      
"""
import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        广度优先搜索，并记录

        """

        h = len(grid)
        w = len(grid[0])

        def bfs(x, y)-> int:
            count = 0
            if grid[x][y]!= 1:
                return count
            q = collections.deque()
            q.append((x, y))
            grid[x][y] = 0
            count += 1
            while q:
                now_x, now_y = q.popleft()
                for new_x, new_y in [(now_x - 1, now_y), (now_x + 1, now_y), (now_x, now_y - 1), (now_x, now_y + 1)]:
                    if 0 <= new_x < h and 0 <= new_y < w and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 0
                        count += 1

            return count

        ans = 0
        for i in range(h):
            for j in range(w):
                ans = max(bfs(i, j),ans)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))

