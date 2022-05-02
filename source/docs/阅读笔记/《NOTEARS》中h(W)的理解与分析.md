# 《NOTEARS》中h(W)的理解与分析

```
@article{zheng2018dags,
  title={Dags with no tears: Continuous optimization for structure learning},
  author={Zheng, Xun and Aragam, Bryon and Ravikumar, Pradeep K and Xing, Eric P},
  journal={Advances in Neural Information Processing Systems},
  volume={31},
  year={2018}
}
```

在论文中，提出了
$$
h(W)=0<=>\text{W is acyclic}
$$
并且$h(W)$ 具有以下性质：

1. 是acyclic的充分必要条件；
2. h量化了图的“有向无环性”；
3. h是光滑的；
4. h和h的导数方便计算。

分两步进行推导，首先考虑特殊情况（binary adjacent matrix），再泛化到一般情况（weighted adjacent matrix）。

## 特殊情况（binary adjacent matrix）

定理1：如果$B\in\{0,1\}^{d\times d}$,且$r(B)<1$，那么B是DAG 当且仅当：
$$
tr(I-B)^{-1}=d
$$
证明：$tr(B^k)$计算的是长度为k的闭环数量，那么当$k=1,2,...,\infty$时， $tr(B^k)=0$均成立，那么说可以说B没有闭环，当且仅当$f(B)=\sum_{k=1}^\infty \sum_{i=1}^d(B^K)_{ii}=0$，写为：
$$
tr(\sum_{k=0}^\infty B^k)
$$
使用等比数列求和公式：
$$
\sum_{k=0}^\infty B^k=B^0+B^1+...+B^\infty=\frac{I-B^\infty}{I-B}
$$
当$r(B)<1$，所以$B^\infty=0$，可以得到$\sum_{k=0}^\infty B^k=(I-B)^{-1}$。将上面两个式子合并，写为:
$$
tr(I-B)^{-1}=tr(\sum_{k=0}^\infty B^k)=trI+\sum_{k=1}^\infty B^k=d+f(B)
$$

> r(B)<1是一个强假设，虽然当B是DAG的时候的确满足，但是其他时候并不能满足。为了避免无限序列情况，将$\sum_{k=0}^\infty B^k$改写为有限序列，使得谱半径假设不再需要。

 最大环的长度是d，所以在此将无限序列改为长度为d的序列。

定理2：如果$B\in\{0,1\}^{d\times d}$，那么B是DAG 当且仅当：
$$
tr(e^B)=d
$$
证明：当$k=1,2,...,d$时， $tr(B^k)=0$均成立，则B为DAG。那么可以推广位为：

当$k=1,2,...,d$时， $tr(B^k/k!)=0$均成立，则B为DAG。

> 矩阵指数的定义：$e^X=\sum_{k=0}^\infty \frac{1}{k!}X^k$

$$
tr(e^B)=tr(I)+tr(\sum_{k=1}^d\frac{1}{k!}B^k)+tr(\sum_{k=d+1}^\infty\frac{1}{k!}B^k)\\
tr(e^B)-d-tr(\sum_{k=d+1}^\infty\frac{1}{k!}B^k)=tr(\sum_{k=1}^d\frac{1}{k!}B^k)
$$

$tr(\sum_{k=d+1}^\infty\frac{1}{k!}B^k)$ 是大于d长度的闭环数目，肯定为0，所以，上式可以最终化简为:
$$
tr(e^B)-d=0
$$

## 一般情况（weighted adjacency matrix）

定理3：将定理2，推广到加权邻接矩阵，对于$W\in R^{d\times d}$，其为DAG，当且仅当：
$$
h(W)=tr(e^{W\circ W })-d=0
$$
且$h(W)$的导数为：
$$
\nabla h(W)=(e^{W\circ W })^T\circ 2W
$$
证明：类似于前面定理1的证明，$tr(B^k)$计算的是长度为k的闭环数量，因为W可能为负数，所以使用哈达玛积（元素对应位置相乘）将路径长度写为$w_{ij}^2$。

## Links

第一篇将代数与环数结合的文献：

```
@article{harary1971number,
  title={On the number of cycles in a graph},
  author={Harary, Frank and Manvel, Bennet},
  journal={Matematick{\`y} {\v{c}}asopis},
  volume={21},
  number={1},
  pages={55--63},
  year={1971},
  publisher={Mathematical Institute of the Slovak Academy of Sciences}
}
```

计算矩阵指数的文献：

```
@article{al2010new,
  title={A new scaling and squaring algorithm for the matrix exponential},
  author={Al-Mohy, Awad H and Higham, Nicholas J},
  journal={SIAM Journal on Matrix Analysis and Applications},
  volume={31},
  number={3},
  pages={970--989},
  year={2010},
  publisher={SIAM}
}
```

