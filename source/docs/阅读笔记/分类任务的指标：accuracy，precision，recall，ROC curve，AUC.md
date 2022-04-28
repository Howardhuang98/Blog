# 分类任务的指标：accuracy，precision，recall，ROC curve，AUC

https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

## 定义TP,FP,FN,TN

![image-20220428171429674](%E5%88%86%E7%B1%BB%E4%BB%BB%E5%8A%A1%E7%9A%84%E6%8C%87%E6%A0%87%EF%BC%9Aaccuracy%EF%BC%8Cprecision%EF%BC%8Crecall%EF%BC%8CROC%20curve%EF%BC%8CAUC.assets/image-20220428171429674.png)

如何计算TP？

True 代表正确，说明模型预测正确；

Positive 代表阳性，代表预测内容为阳性；

TP 是模型正确预测为1（阳性）的概率；

TF是模型正确预测为0的概率；

FN是模型错误预测，模型预测为0的概率；

FP是模型错误预测，模型预测为1的概率。

总结：这是个指标实际上是2*2的组合，针对**模型对错**，**模型预测内容**来说的

## Accuracy

对于二分类问题：
$$
ACC=\frac{TP+TN}{TP+TN+FP+FN}
$$
实际上ACC是一个更加宽泛的指标：
$$
ACC=\frac{Correct\_predictions}{All\_predictions}
$$
但是ACC 并不是一个平衡的准则：当样本的**类别不平衡**的时候，ACC不能说明情况。

## Precision

准确度：模型描述预测1的时候，多少概率是正确的。
$$
Precision=\frac{TP}{TP+FP}
$$

## Recall

回召度：多大的概率1被正确地识别出来。
$$
Recall=\frac{TP}{TP+FN}
$$

## ROC curve

**ROC receiver operating characteristic curve**：描述分类模型在各个阈值下的分类性能。

![ROC Curve showing TP Rate vs. FP Rate at different classification thresholds.](%E5%88%86%E7%B1%BB%E4%BB%BB%E5%8A%A1%E7%9A%84%E6%8C%87%E6%A0%87%EF%BC%9Aaccuracy%EF%BC%8Cprecision%EF%BC%8Crecall%EF%BC%8CROC%20curve%EF%BC%8CAUC.assets/ROCCurve.svg)
$$
TPR=\frac{TP}{TP+FN}
$$

$$
FPR=\frac{FP}{FP+TN}
$$

## AUC

![AUC (Area under the ROC Curve).](%E5%88%86%E7%B1%BB%E4%BB%BB%E5%8A%A1%E7%9A%84%E6%8C%87%E6%A0%87%EF%BC%9Aaccuracy%EF%BC%8Cprecision%EF%BC%8Crecall%EF%BC%8CROC%20curve%EF%BC%8CAUC.assets/AUC.svg)

Area under the ROC curve

AUC 是一个综合的方法评价所有阈值下的模型。

如何理解AUC？

首先它可以理解为TP对于所有阈值的积分，这是一个不考虑阈值的评价指标。

AUC在模型全对的时候为1；

AUC在模型全错的时候为0。

