#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   806.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/12 10:11  
------------      
"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 0
        n = 1
        for char in s:
            if row+widths[ord(char)-ord("a")] >100:
                row = 0
                n += 1
            row += widths[ord(char)-ord("a")]
        return [n,row]

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))