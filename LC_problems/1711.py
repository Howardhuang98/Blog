#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1711.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/27 20:13  
------------      
"""
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        i = -1
        j = -1
        ans = float('+inf')
        for index,w in enumerate(words):
            if w == word1:
                i = index
            if w == word2:
                j = index
            if i>0 and j>0:
                ans = min(abs(i-j),ans)
        return ans