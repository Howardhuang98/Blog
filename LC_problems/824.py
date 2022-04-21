#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   824.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/21 10:49  
------------      
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split(" ")
        for i, word in enumerate(s):
            if word[0].upper() in {'A', 'E', 'I', 'O', 'U'}:
                s[i] = word + "ma"
            else:
                s[i] = word[1:] + word[0] + "ma"

            s[i] = s[i] + "a" * (i + 1)
        return " ".join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.toGoatLatin("I speak Goat Latin"))
