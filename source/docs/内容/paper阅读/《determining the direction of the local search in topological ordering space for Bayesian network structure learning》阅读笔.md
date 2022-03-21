# 《determining the direction of the local search in topological ordering space for Bayesian network structure learning》阅读笔记

## abstract

在拓扑顺序上进行局部搜索是BN结构学习的有效方法。然而，现有的算法主要关注于，随机选取一个odering的近邻，这没有明确的方向，容易在局部最优停下来。本文提出一个新的方法，提升局部搜索的能力，通过决定搜索方向。设定鲁棒的终止条件和插入方法。

## intro

本文的贡献

1. 局部搜索的有效方向。
2. 将DAG转化为等价结构，以重新搜索，跳出局部最优
3. 实验验证

## preliminaries

评分的可分解性：
$$
score(G:D)=\sum _{i=1,...,n}=score(X_i|Pa_{X_i}^{G}:D)
$$
score cache：



ordering 拓扑顺序



基于拓扑顺序的局部搜索主要是下面几步：

1. 初始化
2. 改变ordering里面变量的位置
3. restart
4. conversion将顺序转化为DAG，可以使用K2算法





