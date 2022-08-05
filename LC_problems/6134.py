#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6134.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/31 10:47  
------------      
"""
import collections
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node):
            visited = set()

            memo = {}
            q = collections.deque()
            q.append(node)
            visited.add(node)
            distance = 0
            while q:
                cur = q.popleft()
                memo[cur] = distance
                v = edges[cur]
                if v != -1 and v not in visited:
                    q.append(edges[cur])
                    visited.add(v)
                distance += 1
            return memo

        reach = {}
        a = bfs(node1)
        b = bfs(node2)
        for k, v in a.items():
            if k in b.keys():
                reach[k] = max(a[k], b[k])
        print(reach)
        nodes = []
        m = float('+inf')
        for k, v in reach.items():
            if v < m:
                m = v
                nodes = [k]
            if v == m:
                nodes.append(k)
        if not nodes:
            return -1
        return min(nodes)


if __name__ == '__main__':
    s = Solution()
    print(s.closestMeetingNode([4, 4, 4, 5, 1, 2, 2], node1=1, node2=1))
