#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   使用tushare.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/23 13:56  
------------      
"""
import tushare as ts
df = ts.get_k_data(code='300014')
print(df.head())
df.to_csv('stock_data.csv')