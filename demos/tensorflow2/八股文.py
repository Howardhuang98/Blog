#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   八股文.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/23 11:33  
------------      
"""
# import 模块
# train test
# model
# model.compile
# model.fit
# model.summary

import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense

x = datasets.load_iris().data
y = datasets.load_iris().target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=116)


class MLP(Model):
    def __init__(self):
        super(MLP, self).__init__()
        self.d1 = Dense(3, activation='softmax')

    def call(self, x):
        y = self.d1(x)
        return y

model = MLP()


model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
            metrics=['sparse_categorical_accuracy']
            )

model.fit(x_train,y_train,batch_size=32,epochs=500,validation_split=0.3,validation_data=(x_test,y_test))

model.summary()
