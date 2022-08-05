#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   svm.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/4 16:09  
------------      
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.datasets import make_blobs

if __name__ == '__main__':
    fig, axes = plt.subplots(3, 2)
    for i in range(3):
        X, y = make_blobs(n_samples=20, centers=2)
        ax = axes[i][0]
        ax.scatter(X[:, 0], X[:, 1], c=y)
        ax.set_title("Ground Truth")
        ax = axes[i][1]
        clf = svm.LinearSVC(max_iter=1000000)
        clf.fit(X, y)
        pre_y = clf.predict(X)
        w1, w2, b = clf.coef_[0][0], clf.coef_[0][1], clf.intercept_[0]
        ax.set_title("SVM")
        ax.scatter(X[:, 0], X[:, 1], c=y)
        print(np.linalg.norm(clf.coef_, ord=2))
        ax.axline(xy1=(0, b), slope=-w1 / w2)
        x = 1 / np.linalg.norm(clf.coef_, ord=2)
        cos = w1 / np.linalg.norm(clf.coef_, ord=2)
        h = x / cos
        #ax.axline(xy1=(0, b + h), slope=-w1 / w2)
        #ax.axline(xy1=(0, b - h), slope=-w1 / w2)
    plt.show()
