#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/23 15:38  
------------      
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def draw(ax: mpl.pyplot.Axes, x, ys):
    ax.set_title("This is a title!")
    print(x.shape, ys[0].shape)
    ax.set_prop_cycle(color=['r', 'b', 'yellow'], linestyle=[':', '-', '--'])
    for y in ys:

        error_bar = ax.errorbar(x, y, yerr=30, ecolor='gray', marker='s')
        print(error_bar.lines)
        error_bar.lines[0].set_visible(False)
        line = ax.plot(x, y)
        line[0].set(alpha=0.8)

    ax.text(5, 200, "We have three different lines", fontsize=10)


if __name__ == '__main__':
    print(mpl.style.available)
    mpl.style.use('seaborn')
    fig, axes = plt.subplots(2, 1,dpi=500)
    for ax in axes:
        print(ax.get_position())
        x = np.linspace(0, 100, 50)
        y0 = np.asarray([2 * x + 3 + 5 * np.random.randn() for x in x])
        y1 = np.asarray([3 * x + 3 + 50 * np.random.randn() for x in x])
        y2 = np.asarray([1 * x + 3 + 70 * np.random.randn() for x in x])
        draw(ax, x, [y0, y1, y2])

    fig.savefig("2.png")
