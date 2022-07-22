#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6106.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/25 22:59  
------------      
"""
import collections

from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def bfs(i,g):
            if i not in g.keys():
                return [i]
            q = collections.deque()
            walked = set()
            walked.add(i)
            q.append(i)
            while q:
                cur = q.popleft()
                if cur in g.keys():
                    for x in g[cur]:
                        if x not in walked:
                            q.append(x)
                            walked.add(x)
            return list(walked)
        g = {}
        for u, v in edges:
            g.setdefault(u, [])
            g[u].append(v)
            g.setdefault(v, [])
            g[v].append(u)
        #print(g)
        groups = []
        did = [False]*n
        for i in range(n):
            if i not in did:
                did.add(i)
                group = bfs(i,g)
                groups.append(len(group))
                did |=set(group)
                print(i)
        #print(groups)

        ans = n**2
        for i in groups:
            ans -= i**2
        return ans//2


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs(100000, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
