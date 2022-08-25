#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TEprocess.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/24 21:15  
------------      
"""
import numpy as np

if __name__ == '__main__':
    test_data = np.load("test_data.npy",allow_pickle=True)
    test_label = np.load("test_label.npy",allow_pickle=True)
    print(test_data.shape)
    print(test_label.shape)