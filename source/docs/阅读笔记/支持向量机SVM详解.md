# 支持向量机SVM详解

首先支持向量机分为两类：**线性**支持向量机，非线性支持向量机

学习线性支持向量机的方法有：**间隔最大化**，**软间隔最大化**，**合页损失函数**

学习非线性支持向量机时，利用了**核技巧**，大大缩减了求解的难度，直接利用了线性支持向量机的计算结果

# 线性支持向量机

假设：训练数据集线性可分，并且其超平面为

$$
w^*\cdot x+b^*=0
$$

与之对应的决策函数为：

$$
f(x) = sign(w^*\cdot x+b^*)
$$

---

> 函数间隔：
> $$
> \hat \gamma = y_i(w\cdot x_i +b)
> $$
> 
> 几何间隔；对于样本点$(x_i,y_i)$ ,到超平面$(w,b)$的几何间隔为：
> 
> $$
> \gamma_i=y_i(\frac{w}{||w||}\cdot x_i+\frac{b}{||w||})
> $$

最小几何间隔记录为：

$$
\gamma = \min \gamma_i
$$

## 学习线性支持向量机

### 间隔最大化

对于上面的模型，我们的训练策略为间隔最大化：

最小几何间隔最大化

$$
\max_{w,b} \gamma
$$

将其中的w显式地写出来：

$$
\max _{w,b} \frac{\hat \gamma}{||w||}
$$

$$
s.t. y_i(w\cdot x_i+b)\geq \hat \gamma
$$

如果说我们按比例缩放$w,b$, 会发现超平面没有改变，但是$\gamma$ 在发生变化。换而言之，$\gamma$的取值，对优化的结果不会有影响；所以在此我们把$ \gamma$ 写为 1。$\max \frac{1}{||w||}$ 写为  $\min \frac{1}{2}||w||^2$ ，最终得到：

$$
\begin{array}{ll}
\min _{w, b} & \frac{1}{2}\|w\|^{2} \\
\text { s.t. } & y_{i}\left(w \cdot x_{i}+b\right)-1 \geqslant 0, \quad i=1,2, \cdots, N
\end{array}
$$

这是一个带约束的**凸优化**问题，可使用拉格朗日法求得最优解。



**最大间隔分离超平面的存在唯一性**

证明：

存在性：因为已经假设了数据集线性可分，所以一定存在可行解。

唯一性：

假设现存在两个最优解$(w_1^*,b_1^*),(w_2^*,b_2^*)$ ,进行缩放，得到$||w_1^*||=||w_2^*||=c$ 

对于$(w=\frac{w_1^*+w_2^*}{2},b=\frac{b_1^*+b_2^*}{2})$, 可以由边界条件推出$(w,b)$是可行解:

$$
c\le||w||\le\frac{1}{2}||w_1||+\frac{1}{2}||w_2||=c
$$

因为$||w^*||$是最小值，且为c，所以可以得出：

$$
c\le ||w||
$$

然后根据范数的特征：

$$
c\le||w||\le\frac{1}{2}||w_1||+\frac{1}{2}||w_2||=c
$$

这个不等式可以推出：

$$
||w||=\frac{1}{2}||w_1||+\frac{1}{2}||w_2||
$$

首先，w是$w_1,w_2$组合而来的，现在又说它的长度直接等于其组合，这就表明$w_1$,$w_2$ 是平行的：$w_1^* = \{+,-\} w_2^*$ 

如果是-1，那么w = 0, (0,b)不是可行解；

如果是1，那么这两个假设的超平面写为：$(w^*,b_1^*),(w^*,b_2^*)$ 

现有数据点 $(x_1^{'},-1),(x_1^{''},1),(x_2^{'},-1),(x_2^{''},1)$ 为最近的点，则：

$$
b_{1}^{*}=-\frac{1}{2}\left(w^{*} \cdot x_{1}^{\prime}+w^{*} \cdot x_{1}^{\prime \prime}\right)\\
b_{2}^{*}=-\frac{1}{2}\left(w^{*} \cdot x_{2}^{\prime}+w^{*} \cdot x_{2}^{\prime \prime}\right)
$$

所以：

$$
\begin{aligned}
&w^{*} \cdot x_{2}^{\prime}+b_{1}^{*} \geqslant 1=w^{*} \cdot x_{1}^{\prime}+b_{1}^{*} \\
&w^{*} \cdot x_{1}^{\prime}+b_{2}^{*} \geqslant 1=w^{*} \cdot x_{2}^{\prime}+b_{2}^{*}
\end{aligned}
$$

得到:$w^{*} \cdot\left(x_{1}^{\prime}-x_{2}^{\prime}\right)=0$ , $w^{*} \cdot\left(x_{1}^{\prime \prime}-x_{2}^{\prime \prime}\right)=0$

$$
b_{1}^{*}-b_{2}^{*}=0
$$

这与最初的假设相违背，解的唯一性得证。

#### 支持向量

由上面的推导可以看出，我们寻找的超平面是由两个点决定的：这两个点使约束的等号成立，分别为正负样本。

记录

$$
H_1:w\cdot x_1+b=1 \\
H_2:w\cdot x_2+b=-1 \\
$$

写成几何间隔的话，间隔为：$\frac{2}{||w||}$ 

- 决定分离超平面时，只有支持向量起作用
- 除了支持向量，其他数据点不起作用
- 支持向量得个数一般恒少，所以支持向量机由很少的 “重要” 样本点决定

### 间隔最大化对偶问题

对于一个带约束的凸优化问题；我们可以使用拉格朗日对偶性将其转化为对偶问题。有两点好处：

1. 对偶问题更方便求解；
2. 自然地引入核函数。

首先写出原问题：

$$
\begin{array}{ll}
\min _{w, b} & \frac{1}{2}\|w\|^{2} \\
\text { s.t. } & y_{i}\left(w \cdot x_{i}+b\right)-1 \geqslant 0, \quad i=1,2, \cdots, N
\end{array}
$$

拉格朗日函数为：

$$
L(w,b,\alpha)=\frac{1}{2}\|w\|^{2} - \sum_{i=1}^N \alpha_i y_i(w\cdot x_i +b)+\sum_{i=1}^N \alpha_i
$$

> 记得将约束化为标准形式

对偶问题为：

$$
\max_\alpha \min_{w,b} L(w,b,\alpha)
$$

**第一步**：求解$\min_{w,b}L(w,b,\alpha)$

对w,b求偏导，使其等于0：

$$
\nabla_{w} L(w, b, \alpha)=w-\sum_{i=1}^{N} \alpha_{i} y_{i} x_{i}=0\\
\nabla_{b} L(w, b, \alpha)=\sum_{i=1}^{N} \alpha_{i} y_{i}=0
$$

可以得出：

$$
w = \sum_{i=1}^N \alpha_i y_i x_i
$$

$$
\sum_{i=1}^N \alpha_i y_i =0
$$

把这个带入到拉格朗日函数，以消除w,b:

$$
\min _{w, b} L(w, b, \alpha)=-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_{i} \alpha_{j} y_{i} y_{j}\left(x_{i} \cdot x_{j}\right)+\sum_{i=1}^{N} \alpha_{i}
$$

**第二步**：求max

$$
\max _{\alpha}-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_{i} \alpha_{j} y_{i} y_{j}\left(x_{i} \cdot x_{j}\right)+\sum_{i=1}^{N} \alpha_{i}
$$

$$
s.t. \sum_{i=1}^{N} \alpha_{i} y_{i}=0
$$

$$
\alpha_{i} \geqslant 0, \quad i=1,2, \cdots, N
$$

改写为求min的形式，最终的**对偶问题**为：

$$
\min _{\alpha}\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_{i} \alpha_{j} y_{i} y_{j}\left(x_{i} \cdot x_{j}\right)-\sum_{i=1}^{N} \alpha_{i}
$$

$$
s.t. \sum_{i=1}^{N} \alpha_{i} y_{i}=0
$$

$$
\alpha_{i} \geqslant 0, \quad i=1,2, \cdots, N
$$

求解这个优化问题的最优解$\alpha^*$ 后，可以确定SVM的最终形式。

**总结**：

1. 原问题
2. 对偶问题
3. 求min，求max
4. 得到最优解

### 软间隔最大化

重新温故**线性可分**支持向量机的优化问题：

$$
\begin{array}{ll}
\min _{w, b} & \frac{1}{2}\|w\|^{2} \\
\text { s.t. } & y_{i}\left(w \cdot x_{i}+b\right)-1 \geqslant 0, \quad i=1,2, \cdots, N
\end{array}
$$

函数间隔大于1；让$||w||$ 尽可能小，意味着几何间隔会尽可能的大。

对于**线性不可分**情况，函数间隔大于1的要求我们要放松，加入松弛变量并进行惩罚：

$$
\begin{array}{ll}
\min _{w, b, \xi} & \frac{1}{2}\|w\|^{2}+C \sum_{i=1}^{N} \xi_{i} \\
\text { s.t. } & y_{i}\left(w \cdot x_{i}+b\right) \geqslant 1-\xi_{i}, \quad i=1,2, \cdots, N \\
& \xi_{i} \geqslant 0, \quad i=1,2, \cdots, N
\end{array}
$$

这里我们称之为**软间隔最大化**。

### 合页损失函数

hinge loss function:

$$
[z]_{+}= \begin{cases}z, & z>0 \\ 0, & z \leqslant 0\end{cases}
$$

![img](%E6%94%AF%E6%8C%81%E5%90%91%E9%87%8F%E6%9C%BASVM%E8%AF%A6%E8%A7%A3.assets/v2-3c6aa9626ee8e4609b0d7c5712baf624_1440w.jpg)

合页损失函数的引入，可以实现软间隔最大化：
$$
\min _{w,b} \sum_{i=1}^N[1-y_i(w\cdot x_i+b)]_+ + \lambda ||w||^2
$$

1. 0-1损失函数是二分类问题的真正的损失函数，合页损失函数是0-1损失函数的上界；
2. 0-1损失函数不是连续可导的，直接优化比较困难。

### 软间隔最大化的对偶问题

$$
\max _{\alpha}-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_{i} \alpha_{j} y_{i} y_{j}\left(x_{i} \cdot x_{j}\right)+\sum_{i=1}^{N} \alpha_{i}
$$

$$
\text { s.t. } \quad \sum_{i=1}^{N} \alpha_{i} y_{i}=0
$$

$$
0 \leqslant \alpha_{i} \leqslant C
$$

# 非线性支持向量机

非线性可分的问题：能用 $x\in R^n$ 中的**超曲面**将正负例正确分开，则称这个问题为非线性可分问题。

非线性问题并不好求解，希望能够使用解线性分类问题的方法解决这个问题。进行一个非线性变化，将非线性问题转化为线性问题。

1. 适用于给变换，将原空间的数据映射到新空间
2. 在新空间里用线性分类学习方法从训练数据中学习分类模型

核方法：将输入空间$R^n$对应于一个特征空间 $H$ , 使得输入控件的超曲面模型对应于特征空间里的超平面模型（支持向量机）。

## 核函数

**定义核函数**：

设$X\in R^n$是输入空间，设 $H$ 为特征空间（希尔伯特空间），如果存在一个从 $X-> H$的映射：

$$
\phi(x):X-> H
$$

使得对所有的$x,z \in X$, 函数$K(x,z)$满足条件：

$$
K(x,z) =\phi(x)\cdot \phi(z)
$$

则 $K$ 为核函数，$\phi(x)$ 为映射函数。

**为什么要使用核技巧**：

学习与预测中，我们只需要定义核函数，不需要显式定义映射函数，并不会给计算带来太大的麻烦。

核函数定义了内积的运算，所以在SVM的对偶问题里，可以将内积运算用核函数替代。

在核函数K给定的条件下，可以利用**线性分类问题的方法**（二次凸规划）求解非线性分类问题的支持向量机。

**正定核**

正常来讲，核函数由映射函数计算出来；但是为了方便计算，往往不显式定义映射函数，如何不借助映射函数判断K是否为核函数（核函数就是正定核函数）呢？

**正定核的充要条件**：

假设$K(X\times X)-> R$ 是对称函数，则$K(x,z)$为正定核函数的充要条件是对于任意$x_i\in X,i=1,2,..,m$, $K(x,z)$对应的Gram矩阵：

$$
K = [K(x_i,x_j)]_{m\times m} 
$$

是半正定矩阵。

**常用核函数**

1. 多项式核函数

$$
K(x,z) = (x\cdot z+1)^p
$$

如果采用这个核函数，那么SVM写为：

$$
f(x)=sign(\sum_{i=1}^N\alpha_i^*y_i(x_i \cdot x+1 )^p+b^*)
$$

2. 高斯核

$$
K(x, z)=\exp \left(-\frac{\|x-z\|^{2}}{2 \sigma^{2}}\right)
$$

3. 字符串核函数

定义在离散数据集上，可以用于文本、生物信息数据。

## 学习非线性支持向量机

1. 选取适当的核函数，参数C
2. 求解出$\alpha^*$
3. 使用$\alpha^*$确定SVM的参数

小结：

1. 为什么使用对偶问题？
   1. 对于凸问题，对偶问题的并不会影响到问题的解；
   2. 在对偶问题的解中，分类决策函数只依赖于输入x和训练样本的内积，这一点非常符合核函数的应用。

$$
f(x)=\operatorname{sign}\left(\sum_{i=1}^{N} \alpha_{i}^{*} y_{i}\left(x \cdot x_{i}\right)+b^{*}\right)
$$