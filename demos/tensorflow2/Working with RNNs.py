#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Working with RNNs.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/27 12:00  
------------      
"""
import sys

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Model,layers


class RNN(Model):
    def __init__(self):
        super(RNN,self).__init__()
        self.l = layers.SimpleRNN(units=2)

    def call(self, inputs):
        c = self.l(inputs)
        print(c.shape)
        return c


if __name__ == '__main__':
    print("Python: " + str(sys.version))
    print("Tensorflow version: " + tf.__version__)
    print("Keras version: " + keras.__version__)
    #(samples，timesteps,features)
    x = tf.random.normal(shape=(10,5,2))
    y = tf.random.normal(shape=(10,2))
    dataset = tf.data.Dataset.from_tensor_slices((x,y)).batch(2)
    model = RNN()
    model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
            loss="mse")
    model.fit(dataset)
    model.summary()
    # y = model.predict(x = tf.random.normal(shape=(1,10,5)))
    # print(y)
