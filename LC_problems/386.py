#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   386.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/18 12:54  
------------      
"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(number):
            print(number)
            if number > n:
                return

            if number <= n:
                res.append(number)

            for i in range(0, 10):
                new = int(str(number) + str(i))
                print(new)
                if new != 0:
                    dfs(new)

        dfs(0)
        return res[1:]


if __name__ == '__main__':
    s = Solution()
    print(s.lexicalOrder(2))
