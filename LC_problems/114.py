#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   114.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/31 11:57  
------------      
"""
import collections
import itertools
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = collections.defaultdict(list)
        inDegree = {c: 0 for c in words[0]}
        n = len(words)
        for i in range(n - 1):
            a, b = words[i], words[i + 1]
            for char in b:
                inDegree.setdefault(char, 0)
            for u, v in zip(a, b):
                if u != v:
                    g[u].append(v)
                    inDegree[v] += 1
                    break
            # for仅当 for 循环运行完毕时(即 for 循环没有被 break 语句中止) 才运行 else块
            else:
                print(a, b)
                if len(a) > len(b):
                    return ""
        print(g)
        print(inDegree)
        q = collections.deque()
        ans = []
        for k, v in inDegree.items():
            if v == 0:
                q.append(k)
        while q:
            node = q.popleft()
            ans.append(node)
            for x in g[node]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    q.append(x)
        return ''.join(ans) if len(ans) == len(inDegree) else ""


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
