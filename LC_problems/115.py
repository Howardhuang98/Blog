#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   115.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/23 10:45  
------------      
"""
import collections
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        inDeg = {}
        for seq in sequences:
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i + 1]
                g[u].append(v)
                inDeg.setdefault(u, 0)
                inDeg.setdefault(v, 0)
                inDeg[v] += 1
        #print(g)
        q = collections.deque()
        for k, v in inDeg.items():
            if v == 0:
                q.append(k)
        order = []
        while q:
            if len(q) > 1:
                return False
            cur = q.popleft()
            order.append(cur)
            for node in g[cur]:
                inDeg[node] -= 1
                if inDeg[node] == 0:
                    q.append(node)
        #print(order)
        if order == nums:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2], [1, 3], [2, 3]]))
