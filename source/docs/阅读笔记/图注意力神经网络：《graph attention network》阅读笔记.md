# 图注意力神经网络：《graph attention network》阅读笔记


![image-20220423204253167](%E3%80%8Agraph%20attention%20network%E3%80%8B%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0.assets/image-20220423204253167.png)

## abstract

提出图注意力网络，一个新的基于图结构数据的神经网络构架。借助注意力层来克服图卷积操作的短处。

节点可以参与到邻居节点的特征。

## introduction

卷积操作适用于grid-like structure，卷积网络的构架高效地重复使用local filters。

但是对于别的情况，比如3D meshes， 社交网络，生物学网路来说，他们并不是grid-like data。

已经有一些尝试将神经网络应用在任意结构的图（相比于grid like structure）上。

目前，研究者对使用卷积操作到图领域这件事非常感兴趣，分为两类spectral approach和non-spectral approach。谱方法和非谱方法。

（#TODO: 对于图上卷积操作的review）

本文提出一个基于**注意力机制**的节点分类方法：computing **hidden representations** by attending over its neighbors following a **self-attention** strategy. 

具备以下几个优势：

1. 操作非常高效，parallelizable；
2. 可以适用于具有不同度的节点；
3. 模型适用于 inductive learning problem，包括使用在其他图上。

### GAT architecture

在此描述一层GAT。

**输入**N个节点与其节点特征：$h=[h_1,h_2,...,h_N], h_i \in R^F$

**输出**N个节点与其节点特征，其特征维度更新到 $F'$ ,$h'=[h'_1,h'_2,...,h'_N], h'_i \in R^{F'}$

-----

在这一层中，包括一个**共享的注意力机制**：$a: R^{F'}\times R^{F} \rightarrow R$ 。

$$
e_{ij}=a(Wh_i,Wh_j)
$$

这代表的是对于j节点对于i节点的重要度，使用masked attention，只计算 $e_{ij}$ for node $j\in \mathcal{N_i}$ ，准确地说是一阶的邻居节点。

为了使系数方便比较，将重要度归一化为一个**标量**：

$$
\alpha_{i j}=\operatorname{softmax}_{j}\left(e_{i j}\right)=\frac{\exp \left(e_{i j}\right)}{\sum_{k \in \mathcal{N}_{i}} \exp \left(e_{i k}\right)}
$$

在本文，a是一个单层神经网络，所以综合写为：

$$
\alpha_{i j}=\frac{\exp \left(\operatorname{LeakyReLU}\left(\overrightarrow{\mathbf{a}}^{T}\left[\mathbf{W} \vec{h}_{i} \| \mathbf{W} \vec{h}_{j}\right]\right)\right)}{\sum_{k \in \mathcal{N}_{i}} \exp \left(\operatorname{LeakyReLU}\left(\overrightarrow{\mathbf{a}}^{T}\left[\mathbf{W} \vec{h}_{i} \| \mathbf{W} \vec{h}_{k}\right]\right)\right)}
$$

计算图如左图所示：

![image-20220423213201580](%E3%80%8Agraph%20attention%20network%E3%80%8B%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0.assets/image-20220423213201580.png)

计算完每个边上的“注意力”后，使用一个非线性变换进行更新节点：

$$
\vec{h}_{i}^{\prime}=\sigma\left(\sum_{j \in \mathcal{N}_{i}} \alpha_{i j} \mathbf{W} \vec{h}_{j}\right)
$$

为了稳定学习过程，可以将增加多头注意力，如上图的右图，就是三头注意力。

$$
\vec{h}_{i}^{\prime}=\|_{k=1}^{K} \sigma\left(\sum_{j \in \mathcal{N}_{i}} \alpha_{i j}^{k} \mathbf{W}^{k} \vec{h}_{j}\right)
$$

应为有K个head，所以得到的$h'_i$ 的长度为 KF'，为了避免这种情况，可以让K个head的F'长度的向量取平均值。 

### 个人总结

1. GAT并不使用edge attribution；
2. 适用于节点分类任务。	

### pyG实现

![image-20220423222010470](%E3%80%8Agraph%20attention%20network%E3%80%8B%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0.assets/image-20220423222010470.png)

显然，我们只需要定义好F，和F'，就可以初始化一个注意力图神经网络了。