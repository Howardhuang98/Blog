#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2101.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/8 11:09  
------------      
"""
import collections
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = {}
        for i, b in enumerate(bombs):
            x, y, r = b
            g[i] = []
            for i_, b_ in enumerate(bombs):
                x_, y_, r_ = b_
                if i == i_:
                    continue
                elif r ** 2 >= (x - x_) ** 2 + (y - y_) ** 2:
                    g[i].append(i_)
        print(g)
        ans = 0
        for i in g:
            q = collections.deque([i])
            cnt = 0
            boomed = {i}
            while q:
                current = q.popleft()
                cnt += 1
                for b in g[current]:
                    if b not in boomed:
                        boomed.add(b)
                        q.append(b)
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumDetonation([[2, 1, 3], [6, 1, 4]]))
    print(s.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
