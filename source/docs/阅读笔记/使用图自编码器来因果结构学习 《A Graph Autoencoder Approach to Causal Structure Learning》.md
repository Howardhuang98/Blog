# 使用图自编码器来因果结构学习 《A Graph Autoencoder Approach to Causal Structure Learning》

![image-20220425202021192](%E4%BD%BF%E7%94%A8%E5%9B%BE%E8%87%AA%E7%BC%96%E7%A0%81%E5%99%A8%E6%9D%A5%E5%9B%A0%E6%9E%9C%E7%BB%93%E6%9E%84%E5%AD%A6%E4%B9%A0%20%E3%80%8AA%20Graph%20Autoencoder%20Approach%20to%20Causal%20Structure%20Learning%E3%80%8B.assets/image-20220425202021192.png)

## abstract

NOTEARS方法将组合优化的结构学习问题转化为连续优化问题，使用梯度进行优化。

## Introduction

Zheng 提出了一个 smooth characterization on acyclicity constraint。用h(x)描述有向无环性，且h(x)可导。

## Gradient-based causal structure learning

现有 d 个节点 $x_1,x_2,...,x_d,x \in R^l$ 。

假定数据的生成过程：
$$
x_i = f_i(x_{pa(i)})+z_i
$$
$z \in R^l$ 是噪声。对于线性模型（SEM）来说，符合：
$$
x_i = Xa_i+Z_i
$$
 $A=[a_1,a_2,...,a_d]$

有向无环约束写为:
$$
tr(e^{A\bigodot A})-d=0
$$

## graph autoencoder

![image-20220425203901081](%E4%BD%BF%E7%94%A8%E5%9B%BE%E8%87%AA%E7%BC%96%E7%A0%81%E5%99%A8%E6%9D%A5%E5%9B%A0%E6%9E%9C%E7%BB%93%E6%9E%84%E5%AD%A6%E4%B9%A0%20%E3%80%8AA%20Graph%20Autoencoder%20Approach%20to%20Causal%20Structure%20Learning%E3%80%8B.assets/image-20220425203901081.png)

计算图定义如下：

1. X [d,l]
2. MLP
3. [d,hidden_dim]
4. 与A相乘(线性变换)[d,d\][d,hidden_dim]--->[d,hidden_dim]
5. [d,hidden_dim]
6. MLP
7. [d,l]

## Augmented Lagrangian Method

使用拉格朗日乘子法进行优化。使用的是一阶梯度。

![image-20220425212551312](%E4%BD%BF%E7%94%A8%E5%9B%BE%E8%87%AA%E7%BC%96%E7%A0%81%E5%99%A8%E6%9D%A5%E5%9B%A0%E6%9E%9C%E7%BB%93%E6%9E%84%E5%AD%A6%E4%B9%A0%20%E3%80%8AA%20Graph%20Autoencoder%20Approach%20to%20Causal%20Structure%20Learning%E3%80%8B.assets/image-20220425212551312.png)

优化一系列的拉格朗日函数$L_{\rho,\alpha}^1,L_{\rho,\alpha}^2,...,L_{\rho,\alpha}^k$

根据规则来更新 $\rho,\alpha$，两个量都会越变越大。

![image-20220425213037858](%E4%BD%BF%E7%94%A8%E5%9B%BE%E8%87%AA%E7%BC%96%E7%A0%81%E5%99%A8%E6%9D%A5%E5%9B%A0%E6%9E%9C%E7%BB%93%E6%9E%84%E5%AD%A6%E4%B9%A0%20%E3%80%8AA%20Graph%20Autoencoder%20Approach%20to%20Causal%20Structure%20Learning%E3%80%8B.assets/image-20220425213037858.png)

```python
def train_loop():
    for _ in range(k)
        for _ in range(n):
            # optimize current Lagragian function.
            loss = loss_function(alpha,rho)
            loss.backward()
            optimizor.step()
        update_alpha_and_rho()
```

## 评价

1. 验证只使用了自定函数的合成数据，有可能对其他算法不公平；
2. 充分利用NOTEARS的工作，good。