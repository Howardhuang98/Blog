#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   6079.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/29 21:12  
------------      
"""
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        for i,word in enumerate(words):
            if word[0]=='$' and len(word)>1:
                if word[1:].isdigit() and int(word[1:])>0:
                    words[i] = f'${int(word[1:])*(100-discount)/100:.2f}'
        return " ".join(words)

if __name__ == '__main__':
    s = Solution()
    print(s.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$",50))

