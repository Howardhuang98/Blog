#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6073.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/17 11:33  
------------      
"""
import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re

        data = list(re.split(r', | |', paragraph))
        for i in range(len(data)):
            data[i] = data[i].strip()
        print(data)
        c = collections.Counter(data)
        a = c.most_common()
        print(a)
        for k,v in a:
            if k not in banned:
                return k
if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",banned = ["hit"]))