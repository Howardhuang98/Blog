# Causeme挑战：《Inferring causation from time series in Earth system sciences》阅读
![image-20220519211058417](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519211058417.png)

发表在nature communication上。

## Abstract

科学的本质就是探索现象背后的因果关系；

在大规模的动态系统，比如地球系统，上真实地进行实验往往不可行；

现有的大量的observational和simulated data开启了因果方法的大门；

本文总述了因果推断，并且指出了其在地球科学上的应用;

综述了挑战，并开放了一个benchmark平台。

![image-20220519211826793](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519211826793.png)

## Intro

Reichenbach's common cause principle: if variable are dependent then they are either causal to each other or driven by a common driver. 

不同于概率模型，kernel machines，或者深度学习，which mainly focus on prediction and classification, 因果推断目的在于**发现**与**量化**系统变量之间的因果关系。

但是，因果推断方法在地球科学领域并没有广泛应用，除了模拟，皮尔斯相关系数，回归方法，并没其他的好方法。

工作：1. 提供因果推断在地球系统科学上的案例；2. 强调了地球系统科学上的问题，以及因果推断方法是如何克服的；

## Methodology

### Example application of causal inference methods

![image-20220519212935072](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519212935072.png)

三种方法，用于推断这三个变量的因果关系。GC和相关性数据都导致了unphysical links。Walker circulation （沃克环流，一个广泛接受的气流模型）被PCMCI推断出来。

![image-20220519213407907](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519213407907.png)

In Fig. 1b we highlight the Arctic teleconnection pathways of the stratospheric Polar vortex that were extracted from observational data alone: **here causal inference methods have confirmed previous model simulation studies, finding that Arctic sea ice extent in autumn is an important driver of winter circulation in the mid-latitudes**. 

> 泛泛而谈，并没有详细列举；

![image-20220519214033281](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519214033281.png)

最后，使用传统的回归方法来分析 California Current ecosystem。A
**nonlinear causal state-space reconstruction method** here extracts the underlying ecologically plausible network of interactions, **revealing that sea surface temperatures are a common driver of both sardine and anchovy abundances**.

> 直接说线性回归发现不了因果，Granger causality analysis和 CCM 有一定的作用。

### Overview of causal inference methods

Granger causality：it is the first formalization of a practically quantifiable causality definition from time series. 

![image-20220519214626109](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519214626109.png)

Granger causality test：是否忽略黑色box，可以使得prediction error of Y（t时刻）上升。直观上就是说，如果没有观测X，会导致Y的预测变差，这说明XY存在time lagging causality。

![image-20220519215306565](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519215306565.png)

CCM因果模型。

![image-20220519215452467](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519215452467.png)

使用pc算法进行因果发现：

p=0，就是做独立条件检测

p=1，就是做given 1 condition，the independent test. 

此时得到的skeleton，时间维度上有差异的，直接按时间来确定指向。同一时间步上的不能做orient。

![image-20220519215840593](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519215840593.png)

结构因果模型（NOTEARS）：文中使用的是LiNGAM模型。他能识别出$Y_t\rightarrow X_t $ 因为可以从黑线看出，他们的残差r是与Y独立的。反而言之，如果$X_t\rightarrow Y_t $, 那么拟合线是红线，他们的残差与X并不独立。

> 直观理解：首先y=f(x),和x=f(y)的参数肯定不同，但是可能存在推导关系，这就是为什么导致了红黑线的斜率不相同；
>
> 什么是独立？就是知道一个值你可以猜出下一个值，或者说你敢猜另外一个值（这个说法通用适用于条件概率分布）。在上面的图中，y确定后，r可不能猜；但是在下面，如果知道x，那么r是可以根据这张图来猜的；

![image-20220519221112069](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519221112069.png)

一个因果结构推断算法的简介：a是ground truth，bcdef是各个算法的结果。

### key generic problems in Earth system sciences

![image-20220519221323968](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519221323968.png)

因果假设的检验：使用因果推断来证明hypothesis。

![image-20220519221430298](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519221430298.png)

因果复杂网络的分析：建立网络，并且对其影响力进行探索。

![image-20220519221613688](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519221613688.png)

对于极端影响的可解释原因诊断：比如洪水的发生，由多个影响因素导致。这种有向图比无向图有解释性。

![image-20220519221843435](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519221843435.png)

## challenge

![image-20220519222126414](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519222126414.png)

1. 自相关
2. 时间滞后性
3. 非线性
4. 状态独立性
5. 不同的时间长度
6. 通常假设噪声为高斯噪声，有些过程严重违背
7. 找到相关变量
8. 考虑未观测的变量
9. time subsampling
10. time aggregation
11. 测量误差
12. 选择偏好
13. 离散数据
14. 时间不确定性
15. 样本大小
16. 高维度
17. 不确定估计

## Way Forward

![image-20220519224508861](Causeme%E6%8C%91%E6%88%98%EF%BC%9A%E3%80%8AInferring%20causation%20from%20time%20series%20in%20Earth%20system%20sciences%E3%80%8B%E9%98%85%E8%AF%BB.assets/image-20220519224508861.png)