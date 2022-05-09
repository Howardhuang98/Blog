#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6056.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/8 10:34  
------------      
"""
import functools


class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        @functools.lru_cache()
        def f(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n == 3:
                return 4
            else:
                return (4 + 1) * f(n - 3)

        print(f(4))


if __name__ == '__main__':
    s = Solution()
    s.countTexts("22233")
