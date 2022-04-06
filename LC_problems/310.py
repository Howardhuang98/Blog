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
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = collections.deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        # x 是一个叶子节点
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        print(parents)
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]






if __name__ == '__main__':
    s = Solution()
    print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
