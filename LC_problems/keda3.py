#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   keda3.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/20 19:43  
------------      
"""
import collections


def solu(map):
    n = len(map)
    m = len(map[0])
    gift = None
    for i in range(n):
        for j in range(m):
            if map[i][j] == 8:
                gift = (i, j)

    result = []

    def dfs(loc, path):

        if loc[0] == n - 1 or loc[0] == 0 or loc[1] == m - 1 or loc[1] == 0:
            result.append(path)
            return
        x, y = loc
        for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
            if map[new_x][new_y] != 1 and (new_x, new_y) not in path:
                dfs([new_x, new_y], path + [(new_x, new_y)])

    dfs(gift, [gift])
    return min(result,key=lambda x:len(x))


if __name__ == '__main__':
    print(solu([[0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 8, 1], [1, 0, 1, 1]]))
