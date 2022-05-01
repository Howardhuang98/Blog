#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6054.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/30 23:23  
------------      
"""
import collections
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        man_dis = []
        flame_dis = []

        def bfs(start):
            stop = False
            people = False
            t = 0
            x, y = start
            q = collections.deque([(x, y)])
            walked = set()
            walked.add((x, y))
            distance = 0
            while q:
                size = len(q)
                for i in range(size):
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        stop = True
                    elif x == 0 and y == 0:
                        people = True
                    else:
                        for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] != 2 and (
                                    new_x, new_y) not in walked:
                                q.append((new_x, new_y))
                                walked.add((new_x, new_y))
                distance += 1
                if stop:
                    if not people:
                        return -1
                    else:
                        return t
                if people:
                    t += 1

        ans  = bfs((m - 1, n - 1))
        if not ans:
            return int(1e9)
        else:
            return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumMinutes([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]))
