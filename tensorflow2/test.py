#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/23 10:38  
------------      
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np

x = datasets.load_iris().data
y = datasets.load_iris().target
print(x)
print(y)

# 分割数据集合
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=116)
x_train = x_train.astype(np.float32)
print(x_train,y_train)

train_db = tf.data.Dataset.from_tensor_slices((x_train,y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test,y_test)).batch(32)

w1 = tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1))
b1 = tf.Variable(tf.random.truncated_normal([3],stddev=0.1))

epoch = 100
loss_all = 0
lr = 0.1


for epoch in range(epoch):
    for step,(x_train,y_train) in enumerate(train_db):
        print(x_train,y_train)
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train,w1)+b1
            y = tf.nn.softmax(y)
            y_truth = tf.one_hot(y_train,depth=3)
            loss = tf.reduce_mean(tf.square(y_truth-y))
            loss_all += loss.numpy()

        grads = tape.gradient(loss,[w1,b1])
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
