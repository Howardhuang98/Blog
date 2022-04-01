#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1536.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/31 13:37  
------------      
"""
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break

        ans = 0
        for i in range(n):
            k = -1
            for j in range(i, n):
                if pos[j] <= i:
                    ans += j - i
                    k = j
                    break

            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
            else:
                return -1

        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
