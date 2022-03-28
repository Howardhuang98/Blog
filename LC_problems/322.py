#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   322.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/24 20:12  
------------      
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        动态规划 dp[i]
        """
        if amount == 0:
            return 0
        dp = [0 for i in range(amount + 1)]
        for i in range(1,amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                possible = []
                for c in coins:

                    if i - c >= 1 and dp[i - c] != -1:
                        possible.append(dp[i - c] + 1)
                if possible:
                    dp[i] = min(possible)
                else:
                    dp[i] = -1
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2147483647], 2))
