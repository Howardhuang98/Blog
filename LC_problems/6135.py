#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6135.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/31 11:08  
------------      
"""
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        def find(node):
            cur = node
            found = set()
            found.add(cur)
            visited.add(cur)
            path = [cur]
            while True:
                cur = edges[cur]
                if cur == -1:
                    return -1
                if cur in found:
                    path.append(cur)
                    #print(path)
                    for i,node in enumerate(path):
                        if node == path[-1]:
                            return len(path)-i-1
                if cur in visited:
                    return -1
                found.add(cur)
                visited.add(cur)
                path.append(cur)

        n = len(edges)
        cycles = []
        for node in range(n):
            if node not in visited:
                print(node)
                cycles.append(find(node))

        return max(cycles)

if __name__ == '__main__':
    s = Solution()
    print(s.longestCycle([3,3,4,2,3]))