#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   解方程组.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/1 20:57  
------------      
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve

def func(i,n):
    a,b,c,d = i[0],i[1],i[2],i[3]
    return [
        a*n**3+b*n**2+c*n+d,
        3*a*n**2+2*b*n+c,
        a+b+c+d-100000000,
        3*a+2*b+c-100000000
    ]

r = fsolve(func,x0=[0,0,0,0],args=1/3)

def show(r):
    x = np.arange(0,1,0.01)
    y = r[0]*x**3+r[1]*x**2+r[2]*x+r[3]
    print(y)
    plt.plot(x,y)
    plt.show()

show(r)
