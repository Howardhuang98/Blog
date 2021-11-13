#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   softmax 测试.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/9 16:54  
------------      
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Model,layers

x = tf.random.normal(shape=(1,10))
s = layers.Softmax()
y = s(x)
print(y)