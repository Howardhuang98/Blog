#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   953.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/17 20:06  
------------      
"""
import queue
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, v in enumerate(order):
            d[v] = i + 1

        ws = []
        for word in words:

            w = []
            for char in word:
                w.append(d[char])
            w.append(0)

            if len(ws) > 0:
                ws.append(w)
                if not ws[-1] >= ws[-2]:
                    print(ws[-2], ws[-1])
                    return False
            else:
                ws.append(w)
            #print(ws)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
