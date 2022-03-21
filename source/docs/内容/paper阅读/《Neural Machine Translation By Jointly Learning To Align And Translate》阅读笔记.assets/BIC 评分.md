# BIC 评分

![image-20211126120241965](BIC%20%E8%AF%84%E5%88%86.assets/image-20211126120241965.png)

评分函数可以分为两种：

1. Bayesian scores
2. information-theoretic scores

评分最好是**可分解**，这样可以提高计算效率。

评分需要符合score equivalence，因为对于等价图，评分函数要给定相同的评分

## Bayesian scores

贝叶斯评分函数：给定数据时，图的后验概率。

一般情况下，假设所有的图结构都是同样的概率

## information-theoretic scores

总体表达式为：
$$
S(G, D)=\log [\hat{p}(D \mid G)]-\Delta(D, G)
$$
其中前半部分用log似然来描述data有多符合这个图。后半部分来惩罚图的复杂度。

第一部分写为：
$$
\log {p}(D \mid G)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \frac{N_{i j k}}{N_{i j}}=S_{L L}(G, D)
$$
式中$r_i$ 是 $X_i$ 的状态数

$q_i$ 是父节点的状态数 ：比如说 $X_i$  有 $l,j,k$ 三个父节点，那么$q_i = r_l \times r_j \times r_k$ 

计算方法：先做一个表记录

这里已经固定了i，所以对应的是后面两个求和符号，分别是$r_i$ ，$q_i$ ，一共是 $3 \times 2 = 6$ , 所以要有6个数字相加

|    |父节点状态1|父节点状态2|父节点状态3|
|----| :--- | ---- | ---- |
| $X_i$状态1   | 10 | 15 | 20 |
|  $X_i$状态2  | 10 | 5 | 30          |

$N_{i1}$ = 10 + 10 =20 

$N_{i11}$ = 10

根据上表，建立${N_{i j}}$ 表：

| $N_{i1}$ |  $N_{i2}$     |  $N_{i3}$     |
| -------- | ---- | ---- |
| 20 | 20 | 50       |

对应列相除：

|      |      |      |
| ---- | ---- | ---- |
| 0.5  | 0.75 | 0.4  |
| 0.5  | 0.25 | 0.6  |

求log，再乘上第一个表，得到6个数，全部相加。这就是对于$X_i$的评分。

对于AIC评分，后半部分写为：
$$
F=\sum_{i=1}^{n}\left(r_{i}-1\right) q_{i}\\
S_{A I C}(G, D)=S_{L L}(G, D)-F
$$
对于BIC评分：
$$
S_{B I C}(G, D)=S_{L L}(G, D)-\frac{\log N}{2} \cdot F
$$

## BDeu评分

$$ S_{\text {BDeu }}(G, D)=\log P(G)+\sum_{i=1}^{n} \sum_{j=1}^{q_{i}}\left[\log\frac{\Gamma\left(\frac{N^{\prime}}{q_{i}}\right)}{\Gamma\left(N_{i j}+\frac{N^{\prime}}{q_{i}}\right)}+\sum_{k=1}^{r_{i}} \log \frac{\Gamma\left(N_{i j k}+\frac{N^{\prime}}{r_{i q_{i}}}\right)}{\Gamma\left(\frac{N^{\prime}}{r_{i q_{i}}}\right)}\right] $$

对于一个节点来说：
$$
\sum_{j=1}^{q_{i}}\left[\log\frac{\Gamma\left(\frac{N^{\prime}}{q_{i}}\right)}{\Gamma\left(N_{i j}+\frac{N^{\prime}}{q_{i}}\right)}+\sum_{k=1}^{r_{i}} \log \frac{\Gamma\left(N_{i j k}+\frac{N^{\prime}}{r_{i q_{i}}}\right)}{\Gamma\left(\frac{N^{\prime}}{r_{i q_{i}}}\right)}\right]
$$
展开写，分为两部分：
$$
\sum_{j=1}^{q_{i}}\log\frac{\Gamma\left(\frac{N^{\prime}}{q_{i}}\right)}{\Gamma\left(N_{i j}+\frac{N^{\prime}}{q_{i}}\right)}+\sum_{j=1}^{q_{i}}\sum_{k=1}^{r_{i}} \log \frac{\Gamma\left(N_{i j k}+\frac{N^{\prime}}{r_{i q_{i}}}\right)}{\Gamma\left(\frac{N^{\prime}}{r_{i q_{i}}}\right)}
$$




还是先计算个表出来

|    |父节点状态1|父节点状态2|父节点状态3|
|----| ---- | ---- | ---- |
| $X_i$状态1   | 10 | 15 | 20 |
|  $X_i$状态2  | 10 | 5 | 30    |

