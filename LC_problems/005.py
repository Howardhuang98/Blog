#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   005.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/8 21:10  
------------      
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_id = []
        for word in words:
            i = 0
            for char in set(word):
                n = ord(char) - ord("a")
                i += 2 ** n
            word_id.append(i)
        ans = 0
        for i, wid in enumerate(word_id):
            for j in range(i + 1, len(word_id)):
                if word_id[j] & wid == 0:
                    print(bin(word_id[j]),bin(wid))
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(["a","aa","aaa","aaaa"]))
    #print(s.maxProduct(["abcw","baz","foo","bar","fxyz","abcdef"]))
