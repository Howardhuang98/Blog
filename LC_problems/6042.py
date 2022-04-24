#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6042.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/24 10:34  
------------      
"""
import collections
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:

        saw = set()

        def bfs(ori_x, ori_y, r):
            sq_r = r ** 2
            q = collections.deque()
            q.append((ori_x, ori_y))
            visited = set()
            while q:
                x, y = q.popleft()
                for new_x, new_y in [[x, y + 1], [x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y - 1], [x - 1, y - 1],
                                     [x - 1, y], [x - 1, y + 1]]:
                    if (new_x - ori_x) ** 2 + (new_y - ori_y) ** 2 <= sq_r and (new_x, new_y) not in visited:
                        if (new_x, new_y) not in saw:
                            saw.add((new_x, new_y))
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))

        for x, y, r in circles:
            bfs(x, y, r)
        return len(saw)


if __name__ == '__main__':
    s = Solution()
    print(s.countLatticePoints([[2, 2, 2], [3, 4, 2]]))
    print(s.countLatticePoints([[2, 2, 1]]))
