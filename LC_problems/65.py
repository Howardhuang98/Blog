#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   65.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/5 11:26  
------------      
"""
if __name__ == '__main__':
    while True:
        try:
            a = input()
            b = input()
            longest_str = ""
            if len(b)<len(a):
                a,b = b,a
            for l in range(len(a)+1):
                for left in range(0, len(a)):
                    sub = a[left:left+l]
                    for i in range(len(b) - l):
                        if b[i:i + l] == sub and l > len(longest_str):
                            print(longest_str)
                            longest_str = sub
            print(longest_str)
        except EOFError:
            exit()
