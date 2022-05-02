#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   591.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/2 13:48  
------------      
"""
import re


class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        code = re.sub(r"<!\[CDATA\[.*?]]>", "-", code)
        if not code or code[0] != '<':
            return False
        while i < len(code):
            if code[i] == '<':
                s = re.match(r"^<[A-Z]{1,9}>", code[i:])
                e = re.match(r"^</[A-Z]{1,9}>", code[i:])
                if s:
                    stack.append((i, s.group()))
                elif e:
                    end = e.group()
                    if not stack:
                        return False
                    if stack[-1][1] != '<' + end[2:]:
                        return False
                    j, tag = stack.pop()
                    if i != len(code) - len(tag) - 1 and not stack:
                        return False
                else:
                    return False
            i += 1
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("<![CDATA[ABC]]><TAG>sometext</TAG>"))
