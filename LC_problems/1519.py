#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1519.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 16:17  
------------      
"""
import copy
from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[1]].append(edge[0])
            tree[edge[0]].append(edge[1])

        def dfs(node,pre):
            f[node] = [labels[node]]

            # 探索
            for child in tree[node]:
                if child != pre:
                    dfs(child, node)
                    f[node] += f[child]

        f = {}
        dfs(0,-1)
        return [f[i].count(labels[i]) for i in range(n)]






if __name__ == '__main__':
    s = Solution()
    print(s.countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels="abaedcd"))
    print(s.countSubTrees(4, [[0,1],[1,2],[0,3]], labels="bbbb"))
