#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RNN理解.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/27 20:04  
------------      
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Model,layers


x = tf.random.normal(shape=(3,10,5))
rnn = layers.SimpleRNN(units=1)
y = rnn(x)
print(y.shape)

x = tf.random.normal(shape=(3,10,5))
rnn = layers.SimpleRNN(units=2)
y = rnn(x)
print(y.shape)

x = tf.random.normal(shape=(3,10,5))
rnn = layers.SimpleRNN(units=3)
y = rnn(x)
print(y.shape)

x = tf.random.normal(shape=(3,10,5))
rnn = layers.LSTM(units=3)
y = rnn(x)
print(y.shape)