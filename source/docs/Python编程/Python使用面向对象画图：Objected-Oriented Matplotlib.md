# Python使用面向对象画图：Objected-Oriented Matplotlib

Matplotlib有两种画图风格：

- 面向对象
- state-based interface

在画多个图，或者详细画图时往往使用面向对象风格可以对图片进行更好的操作与管理。

## 面向对象

重要的两个定义：

1. Figure是最终的图，包含1或者多个Axes
2. Axes是一个独立子图
2. 一切可以看到的包括Figure和Figure中的元素都是Artist

Figure是顶级容器；

![](Python%E4%BD%BF%E7%94%A8%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%94%BB%E5%9B%BE%EF%BC%9AObjected-Oriented%20Matplotlib.assets/anatomy.png)

基本步骤：

- 确定图片（关于图片的参数于这里定义）和子图的布局

```python
fig, axes = plt.subplots(2, 1,**kwargs)
#使用关键词定义figure的参数
```

- 对每个ax进行绘制

```python
for ax in axes:
    ax.plot([1, 2, 3], [1, 2, 3])
```

## Some tricks

1. 制作helper function:

```python
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
```

2. 风格化artist：

```python
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
```

![2](Python%E4%BD%BF%E7%94%A8%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%94%BB%E5%9B%BE%EF%BC%9AObjected-Oriented%20Matplotlib.assets/2-16533004287642.png)

3. 使用style sheet 和 rcParams来风格化

[`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams) 是一个字典，其中是画图的默认风格。

```python
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

```python
with mpl.rc_context({'lines.linewidth': 2, 'lines.linestyle': ':'}):
    plt.plot(data)
```

或者使用style sheet，这是存储的风格：

```python
print(plt.style.available)
plt.style.use('seaborn')
```

## Artist

每个图上的元素都是Artist，e.g., axis, line, marker.

Artist有一些共同属性：

alpha: 透明度

zorder：叠加层

visible: 可以让某些方法画的多余的元素隐藏

## 进阶操作

使用cycler进行风格化。比如说一张图上有多个线条，每个线条要使用不同的风格。

```python
ax.set_prop_cycle(color=['r', 'b', 'blue'], linestyle=[':', '-', '--'])
```

> 它需要在画图前指定；**后面的关键字参数可以是任何artist参数**

![img](Python%E4%BD%BF%E7%94%A8%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%94%BB%E5%9B%BE%EF%BC%9AObjected-Oriented%20Matplotlib.assets/handout-tips.png)
