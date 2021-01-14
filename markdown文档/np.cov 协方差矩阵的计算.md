# np.cov 协方差矩阵的计算

![img](C:\Users\admin\iCloudDrive\学习资料\python学习\32ab8c25259851a89027c916cc506e27.svg)

这是X,Y个随机变量之间的协方差计算公式，可以推广到n维矩阵上。

```python
def cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None,aweights=None):
```

```
m : array_like

​    A 1-D or 2-D array containing multiple variables and observations.

​    Each row of `m` represents a variable, and each column a single

​    observation of all those variables. Also see `rowvar` below.
```

注意此处，一列column是一组observation，也就是一组数据。放在常规数据中，我们要转置一下。

```
y : array_like, optional
        An additional set of variables and observations. `y` has the same form
        as that of `m`.
```

```
rowvar : bool, optional
        If `rowvar` is True (default), then each row represents a
        variable, with observations in the columns. Otherwise, the relationship
        is transposed: each column represents a variable, while the rows
        contain observations.
```

此参数是rowvar = True，意思是每行是变量。

```
bias : bool, optional
        Default normalization (False) is by ``(N - 1)``, where ``N`` is the
        number of observations given (unbiased estimate). If `bias` is True,
        then normalization is by ``N``. These values can be overridden by using
        the keyword ``ddof`` in numpy versions >= 1.5.
```

无偏估计or有偏估计

```
ddof : int, optional
        If not ``None`` the default value implied by `bias` is overridden.
        Note that ``ddof=1`` will return the unbiased estimate, even if both
        `fweights` and `aweights` are specified, and ``ddof=0`` will return
        the simple average. See the notes for the details. The default value
        is ``None``.
```

```
fweights : array_like, int, optional
        1-D array of integer frequency weights; the number of times each
        observation vector should be repeated.

        .. versionadded:: 1.10
    aweights : array_like, optional
        1-D array of observation vector weights. These relative weights are
        typically large for observations considered "important" and smaller for
        observations considered less "important". If ``ddof=0`` the array of
        weights can be used to assign probabilities to observation vectors.

        .. versionadded:: 1.10
```

返回一个ndarry，协方差矩阵

## 函数分析：



