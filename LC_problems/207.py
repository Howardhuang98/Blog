#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   207.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/22 15:50  
------------      
"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        inDeg = {}
        for v, u in prerequisites:
            g[u].append(v)
            inDeg.setdefault(v, 0)
            inDeg.setdefault(u, 0)
            inDeg[v] += 1
        print(g,inDeg)
        q = collections.deque()
        for k, v in inDeg.items():
            if v == 0:
                q.append(k)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for x in g[node]:
                inDeg[x] -= 1
                if inDeg[x] == 0:
                    q.append(x)
        return True if len(ans) == len(inDeg) else False


if __name__ == '__main__':
    s = Solution()
    s.canFinish(3, [[2, 0], [2, 1]])
