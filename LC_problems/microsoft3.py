#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   microsoft3.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/19 19:09  
------------      
"""
import collections
import math


def solu(A: list, B: list, N: int) -> int:
    g = {}
    peopleMap = {}
    for a, b in zip(A, B):
        g.setdefault(a, [])
        g.setdefault(b, [])
        g[a].append(b)
        g[b].append(a)
        peopleMap.setdefault(a, 1)
        peopleMap.setdefault(b, 1)

    visited = set()

    def fuel(node):
        visited.add(node)
        print(node)
        if not g[node]:
            return 0

        f = 0
        people = 0
        for neighbor in g[node]:
            if neighbor in visited:
                continue
            f += fuel(neighbor) + math.ceil(peopleMap[neighbor] / 5)
            people += peopleMap[neighbor]
            peopleMap[neighbor] = 0
        peopleMap[node] += people

        return f

    res = fuel(0)
    print(peopleMap)
    return res


if __name__ == '__main__':
    print(solu([0, 1, 1], [1, 2, 3], 3))
    print(solu([1, 1, 1, 9, 9, 9, 9, 7, 8], [2, 0, 3, 1, 6, 5, 4, 0, 0], 9))
