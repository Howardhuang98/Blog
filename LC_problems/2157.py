#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2157.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/3 20:15  
------------      
"""
if __name__ == '__main__':
    while True:
        try:
            n, V = list(map(int, input().strip().split()))
            items = []
            for i in range(n):
                v, w = list(map(int, input().strip().split()))
                items.append([v, w])
            # dp[i][j] 装前i个的物品，背包体积为v，价值的最大价值
            dp = [[0 for j in range(V + 1)] for i in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, V + 1):
                    v, w = items[i - 1]
                    if j - v >= 0:
                        dp[i][j] = max(dp[i - 1][j], w + dp[i - 1][j - v])
                    else:
                        dp[i][j] = dp[i - 1][j]
            print(dp[-1][-1])

            # dp[i][j] 装前i个的物品，背包体积为v且装满，价值的最大价值
            dp = [[0 for j in range(V + 1)] for i in range(n + 1)]
            for j in range(1, V + 1):
                for i in range(1, n + 1):
                    v, w = items[i - 1]
                    if j - v >= 0:
                        if dp[i - 1][j - v] != 0 or j-v ==0:
                            dp[i][j] = max([dp[i - 1][j - v] + w, dp[i - 1][j]])
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
            print(dp[-1][-1])

        except EOFError:
            break
