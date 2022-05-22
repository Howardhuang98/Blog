#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   小提琴图.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/30 21:53  
------------      
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\admin\iCloudDrive\学习资料\贝叶斯网络科研\贝叶斯网络集成学习\工作簿1.xlsx",sheet_name='Sheet5')
print(data)
# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data=data)
sns.despine(left=True)
plt.show()