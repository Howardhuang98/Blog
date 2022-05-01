#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6051.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/30 22:31  
------------      
"""
from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        map = [[1 for i in range(n)] for j in range(m)]
        for w in walls:
            x, y = w
            map[x][y] = 'w'
        for g in guards:
            x, y = g
            look_x, look_y = x, y
            while 0 <= look_x < m and map[look_x][look_y] != 'w':
                map[look_x][look_y] = 0
                look_x += 1

            look_x, look_y = x, y
            while 0 <= look_x < m and map[look_x][look_y] != 'w':
                map[look_x][look_y] = 0
                look_x -= 1

            look_x, look_y = x, y
            while 0 <= look_y < n and map[look_x][look_y] != 'w':
                map[look_x][look_y] = 0
                look_y += 1

            look_x, look_y = x, y
            while 0 <= look_y < n and map[look_x][look_y] != 'w':
                map[look_x][look_y] = 0
                look_y -= 1
        for w in walls:
            x,y = w
            map[x][y]=0

        for i in range(m):
            print(map[i])
        return sum([sum(i) for i in map])


if __name__ == '__main__':
    s = Solution()
    print(s.countUnguarded(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]))
