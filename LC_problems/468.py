#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   468.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/29 15:15  
------------      
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def check_4(s: str):
            if s[0] == '0':
                if len(s) == 1:
                    return True
                else:
                    return False
            else:
                if s.isdigit():
                    if 0 <= int(s) <= 255:
                        return True
                    else:
                        return False

        def check_6(s: str):
            if 1>len(s) or len(s)>4:
                return False

            for char in s:
                if ord('0') <= ord(char) <= ord('9') or ord('a') <= ord(char) <= ord('f') or ord('A') <= ord(
                        char) <= ord('F'):
                    continue
                else:
                    return False
            return True

        if '.' in list(queryIP):
            parts = queryIP.split('.')
            for p in parts:
                if not check_4(p):
                    return "Neither"
            return "IPV4"
        elif ':' in list(queryIP):
            parts = queryIP.split(':')
            for p in parts:
                if not check_6(p):
                    return "Neither"
            return "IPV6"


if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
