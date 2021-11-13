#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   三次样条插值.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/2 10:23  
------------      
"""
import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib import pyplot as plt

X = [0,0.3**2,1]
Y = [-10000,0,1000000]

c = CubicSpline(X,Y,bc_type=((1,-10000),(1,10000)))

x = np.linspace(0,1,100)
plt.plot(x,c(x),'-',X,Y,'o')
plt.show()

X = [0.3,1]
Y = [0,1000000]

c = CubicSpline(X,Y,bc_type=((1,0),(1,10000)))

x = np.linspace(0,1,100)
plt.plot(x,c(x),'-',X,Y,'o')
plt.show()