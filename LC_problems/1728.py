#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1728.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/10 22:30  
------------      
"""
import collections
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        reach = [[float("+inf")] * len(grid[0]) for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'C':
                    cat_location = (i, j)
                if grid[i][j] == 'M':
                    mouse_location = (i, j)
                if grid[i][j] == 'F':
                    food_location = (i, j)

        def bsf(start):
            q = collections.deque([start])
            distance = 0
            walked = set()
            walked.add(start)
            while q:
                size = len(q)
                for i in range(size):
                    x, y = q.popleft()
                    reach[x][y] = int(distance / catJump)
                    for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in walked and \
                                grid[new_x][new_y] != '#':
                            q.append((new_x, new_y))
                            walked.add((new_x, new_y))
                distance += 1

        bsf(cat_location)
        print(reach)

        step = [[float("+inf")] * len(grid[0]) for _ in grid]
        def mouse_run(start):
            q = collections.deque([start])
            distance = 0
            walked = set()
            walked.add(start)
            while q:
                size = len(q)

                for i in range(size):
                    x, y = q.popleft()
                    step[x][y]=int(distance/mouseJump)
                    for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in walked and \
                                grid[new_x][new_y] != '#' and int(distance / mouseJump) < 1000:
                            q.append((new_x, new_y))
                            walked.add((new_x, new_y))
                    distance += 1


        mouse_run(mouse_location)
        print(step)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if reach[i][j]<=step[i][j]:
                    step[i][j] = float("+inf")
        print(step)


if __name__ == '__main__':
    s = Solution()
    print(s.canMouseWin(["####F","#C...","M...."], catJump = 1, mouseJump = 2))
