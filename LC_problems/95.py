#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   95.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 10:41  
------------      
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        动态规划
        dp[i][j]:tex1[:i+1]和text2[:j+1]最大公共子序列
        """
        l2 = len(text2)
        l1 = len(text1)
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            if i == 0:
                if text1[i] == text2[0]:
                    dp[0][0] = 1
                else:
                    dp[0][0] = 0
            else:
                if text1[i] == text2[0]:
                    dp[i][0] = 1
                else:
                    dp[i][0] = dp[i - 1][0]

        for j in range(1, l2):
            if text2[j] == text1[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1,l1):
            for j in range(1,l2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i][j])
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence(text1="ac", text2="acc"))
    print(s.longestCommonSubsequence("bsbininm","jmjkbkjkv"))
