#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   987.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/4 21:12  
------------      
"""
if __name__ == '__main__':
    while True:
        try:
            n = int(input().strip())
            data = [float("+inf")]
            for _ in range(n):
                num = int(input())
                size = len(data)
                for i in range(size):
                    if data[i] > num:
                        data = data[:i]+[num]+data[i:]
                        break
                    elif data[i] == num:
                        break
                    else:
                        continue
            for i in data[:-1]:
                print(i)
        except EOFError:
            exit()


