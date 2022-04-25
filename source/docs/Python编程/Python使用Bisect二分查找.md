# Python使用Bisect二分查找

二分查找最关键的问题是边界问题，如果自己实现一定要注意左右边界的含义。

对于一个有序序列而言，`bisect.bisect_left(a, x, [lo=0, hi=len(a)])` 找到索引`i`，满足下列条件：

1. a[:i]<x
2. a[i:]>=x

如何理解这个bisect_left的left？

当出现多个重复数字的时候，比如`[1,2,2,2,3]`，使用`bisect.bisect_left` ，得到的index是1，它位于**相同数字的最左端**，可以理解为**偏左搜索**。

## Api

```PYTHON
bisect_left()
bisect_right()
insort_left()
insort_right()
```

