#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   884.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 19:16  
------------      
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = set()
        removed = set()
        for s in s1.split(" "):
            if s in ans:
                ans.discard(s)
                removed.add(s)
                continue
            elif s in removed:
                continue
            else:
                ans.add(s)
        for j in s2.split(" "):
            if j in ans:
                ans.discard(j)
                removed.add(j)
            elif j in removed:
                continue
            else:
                ans.add(j)
        return list(ans)