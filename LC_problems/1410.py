#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1410.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/12 16:18  
------------      
"""


class Solution:
    def entityParser(self, text: str) -> str:
        l = 0
        r = 0
        reading = False
        result = ""
        convert = {
            "&quot;": "\"",
            "&apos;": "\'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        for i, char in enumerate(text):
            if reading:
                if char == ";":
                    r = i
                    if text[l:r + 1] not in convert.keys():
                        result += text[l:r + 1]
                    else:
                        result += convert[text[l:r + 1]]
                    r = 0
                    l = 0
                    reading = False
                elif char == "&":
                    r = i
                    result += text[l:r]
                    l = i
                    continue
            else:
                if char == "&":
                    l = i
                    reading = True
                    continue
                result += char
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.entityParser("&&&"))
