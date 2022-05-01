#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6053.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/30 23:03  
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
            map[x][y] = 'g'
        for g in guards:
            x, y = g
            look_x, look_y = x+1, y
            while 0 <= look_x < m and map[look_x][look_y] != 'w' and map[look_x][look_y] != 'g':
                map[look_x][look_y] = 0
                look_x += 1

            look_x, look_y = x-1, y
            while 0 <= look_x < m and map[look_x][look_y] != 'w' and map[look_x][look_y] != 'g':
                map[look_x][look_y] = 0
                look_x -= 1

            look_x, look_y = x, y+1
            while 0 <= look_y < n and map[look_x][look_y] != 'w' and map[look_x][look_y] != 'g':
                map[look_x][look_y] = 0
                look_y += 1

            look_x, look_y = x, y-1
            while 0 <= look_y < n and map[look_x][look_y] != 'w' and map[look_x][look_y] != 'g':
                map[look_x][look_y] = 0
                look_y -= 1
        for w in walls:
            x, y = w
            map[x][y] = 0

        for g in guards:
            x, y = g
            map[x][y] = 0
        return sum([sum(i) for i in map])

if __name__ == '__main__':
    s = Solution()
    print(s.countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))
