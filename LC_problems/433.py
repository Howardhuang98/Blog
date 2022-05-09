#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   433.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/7 23:40  
------------      
"""
import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def count(a, b):

            n = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    n += 1
            return n

        def bfs(start):
            q = collections.deque([start])
            did = set([start])
            distance = 1
            while q:
                size = len(q)
                for i in range(size):
                    gene = q.popleft()
                    if gene == end:
                        return distance
                    for new in bank:
                        if count(new, gene) == 1 and new not in did:
                            q.append(new)
                            did.add(new)
                distance += 1
            return -1

        return bfs(start)

if __name__ == '__main__':
    s = Solution()
    s.minMutation("AACCGGTT","AACCGGTA",[])