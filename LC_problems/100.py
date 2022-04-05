#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   100.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/5 11:58  
------------      
"""
import itertools

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            data = list(map(int, input().split(" ")))
            dp = [1 for i in data]
            # dp[i]  [0:i+1]的最长递增子序列
            for i in range(1, len(dp)):
                possible = [1]
                for j in range(i):
                    if data[j] < data[i]:
                        possible.append(dp[j] + 1)
                dp[i] = max(possible)
            dp_r = [1 for i in data]
            for i in range(len(dp_r) - 1, -1, -1):
                possible = [1]
                for j in range(i, len(dp_r)):
                    if data[j] < data[i]:
                        possible.append(dp_r[j] + 1)
                dp_r[i] = max(possible)
            ans = 30000
            for i in range(len(dp)):
                ans=min(len(data)-(dp[i]+dp_r[i]-1),ans)
            print(ans)
        except EOFError:
            exit()
