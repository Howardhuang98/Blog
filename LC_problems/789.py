#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   789.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/12 10:24  
------------      
"""
import collections
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def bfs(start: tuple, end: tuple, max: int):
            if start == end:
                return 0
            q = collections.deque([start])
            distance = 1
            visited = set()
            visited.add(start)
            while q and distance <= max:
                size = len(q)
                for i in range(size):
                    x, y = q.popleft()
                    for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                        if (new_x, new_y) not in visited:
                            visited.add((new_x, new_y))
                            q.append((new_x, new_y))
                            if (new_x, new_y) == end:
                                return distance
                distance += 1
            return -1

        d = bfs((0, 0), tuple(target), 10000)
        for gx, gy in ghosts:
            distance = bfs((gx, gy), tuple(target), d)
            if distance != -1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.escapeGhosts([[2,0]],[1,0]))

