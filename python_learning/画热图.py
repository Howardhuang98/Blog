#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   画热图.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/19 20:13  
------------      
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_excel(r"C:\Users\admin\iCloudDrive\学习资料\贝叶斯网络科研\基于专家信息融合的贝叶斯网络的可靠性分析方法\罗\expert_knowledge2.xlsx")