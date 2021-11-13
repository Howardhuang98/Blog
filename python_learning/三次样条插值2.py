#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   三次样条插值2.py
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/2 11:09  
------------      
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

X = [0,0.3**2,1]
Y = [-1000000,0,1000000]

q = interp1d(X,Y,kind='linear')

x = np.linspace(0,1,100)
plt.plot(x,q(x),'-',X,Y,'o')
plt.show()