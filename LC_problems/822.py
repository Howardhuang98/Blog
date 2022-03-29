#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   822.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/29 13:19  
------------      
"""
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = float('+inf')
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                continue
            for x in [fronts[i], backs[i]]:
                success = True
                for j in range(len(fronts)):
                    if j == i:
                        continue
                    if x != fronts[j] or x != backs[j]:
                        continue
                    else:
                        success = False
                        break
                if success:
                    ans = min(ans, x)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.flipgame([1],[1]))