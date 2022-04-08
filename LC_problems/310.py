#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   310.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/6 16:06  
------------      
"""
import collections
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q




if __name__ == '__main__':
    s = Solution()
    print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
