#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   biset学习.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/25 22:11  
------------      
"""
import bisect
import random

if __name__ == '__main__':
    a = [i for i in range(10)]
    print(a)
    index = bisect.bisect_left(a,5)
    print(index)
    index = bisect.bisect_left(a, 5.1)
    print(index)
    index = bisect.bisect_left(a, 6)
    print(index)
    index = bisect.bisect_right(a, 5)
    print(index)
    index = bisect.bisect_right(a, 5.1)
    print(index)
    index = bisect.bisect_right(a, 6)
    print(index)