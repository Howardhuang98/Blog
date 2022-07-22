#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   091.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/25 11:01  
------------      
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[i for i in costs[0]] for _ in costs]
        for i in range(1,len(dp)):
            for j in range(3):
                if j == 0:
                    dp[i][j] = min(costs[i][j]+dp[i-1][1],costs[i][j]+dp[i-1][2])
                elif j == 1:
                    dp[i][j] = min(costs[i][j] + dp[i - 1][0], costs[i][j] + dp[i - 1][2])
                else:
                    dp[i][j] = min(costs[i][j] + dp[i - 1][0], costs[i][j] + dp[i - 1][1])
        #print(dp)
        return min(dp[-1])
if __name__ == '__main__':
    s = Solution()
    print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))