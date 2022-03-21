# python的语言特性

## 向下取整与四舍五入

divmod()

取下限用 int(1.5)=1

round(1.5) = 2

## 序列类型 list，tuple，range

tuple是不可变的，但是是hashable的

range也是不可变的

## 字符串 str

不可变，hashable

有一些比较使用的方法：

str.count()

str.join()

str.split()

## 集合类型

集合是无序的，没办法索引，但是可以去重。

## 映射类型 dict

键要求hashable

dict.keys()

dict.values()

dict.items()

## 双向队列

collections.deque

Deque队列是由栈或者queue队列生成的（发音是 “deck”，”double-ended queue”的简称）。Deque 支持线程安全，内存高效添加(append)和弹出(pop)，从两端都可以，两个方向的大概开销都是 O(1) 复杂度。

list如果从前面弹出，需要耗费O(n)时间，不建议当成队列使用。

## 计数器

collections.Counter 

## python的数据结构

### 栈

使用list来做栈

append

pop

### 队列

用双向列表实现

```python
from collections import deque
append
popleft
```

### 树

一般是已经规定好了。

### 图

```python
from collections import defaultdict

g = defaultdict(list)
# 这是一个默认字典，可以直接g[node].append[node],即使当前node并未存入键中
```

