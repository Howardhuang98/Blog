#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   TE.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/10 22:25  
------------      
"""
import numpy as np

if __name__ == '__main__':
    data = np.load(r"I:\TEmodel\test_data.npy")
    print(data.shape)
    data = np.load(r"I:\TEmodel\train_data.npy")
    print(data.shape)
    data = np.load(r"I:\TEmodel\train_label.npy")
    print(data.shape)