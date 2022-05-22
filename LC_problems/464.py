#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   464.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/22 13:59  
------------      
"""
import copy


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        def dfs(usedNumbers: int, currentTotal: int, s) -> bool:
            print("\t" * s, usedNumbers, currentTotal)
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal:
                        print("\t" * s, "True")
                        return True
                    if not dfs(usedNumbers | (1 << i), currentTotal + i + 1, s + 1):
                        print("\t" * s, "True")
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.canIWin(3, 2))
