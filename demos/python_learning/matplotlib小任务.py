#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   matplotlib小任务.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/25 13:16  
------------      
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel(r'C:\Users\admin\iCloudDrive\学习资料\贝叶斯网络科研\基于专家信息融合的贝叶斯网络的可靠性分析方法\罗\画bar图.xlsx')
x = data.columns.values
y = data.iloc[0]

plt.figure()

plt.bar(x=x,height=y)

plt.show()