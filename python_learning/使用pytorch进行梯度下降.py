#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :
使用pytorch进行梯度下降.py
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/8 16:08  
------------      
"""
import matplotlib.pyplot as plt
import numpy as np
import torch

if __name__ == '__main__':
    A = torch.tensor(np.random.random([1, 5]))
    x = torch.tensor(np.random.random([5, 1]), requires_grad=True)
    b = torch.tensor(0)
    history = []
    for i in range(200):
        y = torch.pow(torch.matmul(A, x) + b, 2)
        t = 0.005
        history.append(y.data)
        y.backward()
        with torch.no_grad():
            x = x - t * x.grad
            x = x.clone().detach().requires_grad_(True)
            x.grad = None

    plt.plot(history)
    plt.show()
