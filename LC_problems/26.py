#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   26.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/4 21:34  
------------      
"""
import copy

if __name__ == '__main__':
    while True:
        try:
            s = list(input())
            delta = ord("a") - ord("A")
            remain = [i for i in s]
            for index in range(len(s)):
                if s[index].isalpha():
                    current = 100000
                    to_exchange = -1
                    for j in range(0, len(remain)):
                        if remain[j].isalpha():
                            asci = ord(remain[j])
                            if ord('a') <= asci:
                                asci -= delta
                            if asci < current:
                                to_exchange = j
                                current = asci
                    print(to_exchange)
                    s[index] = remain[to_exchange]
                    remain[to_exchange] = " "
            print("".join(s))

        except EOFError:
            exit()
