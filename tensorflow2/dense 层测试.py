#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   dense 层测试.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/11/9 9:43  
------------      
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Model,layers

dense = layers.Dense(1)
x = tf.random.normal(shape=(10,5,128))
y = dense(x)
print(y.shape)