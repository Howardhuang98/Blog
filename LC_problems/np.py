#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   np.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/7/28 19:08  
------------      
"""
import numpy as np

if __name__ == '__main__':
    a = np.random.randn(25,25,3)
    b = np.random.randn(3,256)
    print(np.dot(a,b).shape)