#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/18 20:20  
------------      
"""
# python 画概率密度图
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

if __name__ == '__main__':
    matrix = np.random.randn(30, 30)
    matrix[np.eye(30, dtype=np.bool)] = 0
    fig, ax = plt.subplots()
    ax.matshow(matrix,cmap='gist_rainbow')
    ax.set_yticks([])
    ax.set_xticks([])
    plt.show()
    fig.savefig("matrix.png")
