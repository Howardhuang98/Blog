# 算法练习笔记 I

以此笔记本记录算法题目的解题思路与题型分类。

本笔记本以实战编程为主，理论与思想主要写在《算法导论》阅读笔记中。

[toc]

## ACM模式

一般情况下，会给**多组**数据！

一组数据的格式会给定。

```python
import sys
for line in sys.stdin:
    a = line.split()
    print(a)
```

strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

### 单行输入

```python
in_list = list(map(lambda x:int(x),input().strip().split()))
print(in_list)
```

### 多行输入

```python
while True:
		try:
            line = input().strip()
            print(line)
            # 指定情况终止
            if line == '0 0':
                break
        except:
            break
```

## 数据结构

### 链表-两数之和

https://leetcode-cn.com/problems/add-two-numbers/

### 前缀树Trie

Trie树，即字典树，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较。

```python
class TrieNode:
    """
    前缀树的链式存储
    """
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]
```

### 找出自除数

https://leetcode-cn.com/problems/self-dividing-numbers/

这道题需要解决的问题是如何找出n的每一位数？

1. str()
2. n,d = divmod(n,10)

### 线段树

线段树是一个二叉树。

节点保存 [start,end]的最小值，最大值，和总和等信息

给定数组：[1,5,3,7,3,2,5,7]

![segment tree interval representation](%E7%AE%97%E6%B3%95%E7%BB%83%E4%B9%A0%E7%AC%94%E8%AE%B0.assets/70.png)

线段树的构建是自顶向上的！！

### **差分数组

https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/

我们要维护一个数组;

对数组的操作是 nums[a:b]这个区间内所有的元素+1;

为了避免 for n in nums[a:b]，可以使用差分数组，diff[a]+1,diff[b]-1来记录

nums[i] = sum(diff[:i])

## 双指针，滑动窗口

#### 排序+双指针

https://leetcode-cn.com/problems/3sum/

本来是N\^3算法，通过双指针降低为N\^2。

#### 如果相邻两个颜色均相同则删除

https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

使用一个滑动窗口来寻找连续的相同颜色，并记录。

#### 有效的山脉数组

https://leetcode-cn.com/problems/valid-mountain-array/

双指针夹心

#### 和大于等于target的最短子数组

#### 滑动窗口模板

```
初始化左边界 left = 0
初始化返回值 ret = 最小值 or 最大值
for 右边界 in 可迭代对象:
	更新窗口内部信息
	while 根据题意进行调整：
		比较并更新ret(收缩场景时)
		扩张或收缩窗口大小
	比较并更新ret(扩张场景时)
返回 ret
```

#### 仅仅翻转字母

https://leetcode-cn.com/problems/reverse-only-letters/

使用双指针或者栈

栈是一个高效的翻转工具。

#### 乘积小于k的子数组

https://leetcode-cn.com/problems/subarray-product-less-than-k/

滑动窗口，主要问题是，窗口扩张和未扩展之前的子数组增加数量的计算。

#### 搜索旋转排序数组

当数组是局部有序的，还是可以使用二分查找！

#### 盛最多水的容器

双指针，对于盛水问题，双指针收缩时有一个原则：

**放弃当前的短板**，往内侧收缩才**有可能**使得盛更多的水！

### 二分查找

```python
def binary_search(a,target):
	l = 0
    r = len(a)# 二分查找并不包括右边界
    while l<r-1:
        M = (L + R) // 2
        #逻辑操作
 		#对比a[M]与target的大小
        #更新L或者R
        #更新要注意等号条件，等号应该给到左边界
    return L
```

#### 每个小孩最多能分到多少糖果

https://leetcode-cn.com/problems/maximum-candies-allocated-to-k-children/

#### 绝对插值和（非侵入式二分）

最原始的遍历方法是 10^5 *10^5 , $O(n^2)$ 的方法，通过引入二分查找来做成$O(nlgn)$，一般情况下，n=10^5

 二分查找时候要注意侵入与非侵入：

当我们的范围定义为`[l,r)` 的时候，`l = mid` 保留了这个mid值，但是`r=mid`就会删除mid值。为了保留mid，要做`r=mid+1`

## 递归算法

### 二叉树

二叉树有两种存储方式，一种是用指针存储，一种是使用顺序存储。

顺序存储：如果一个结点在数组的下标为 $node$，那么它的左子结点下标为 $\textit{node} \times 2 + 1$，右子结点下标为  $node×2+2$

![img](%E7%AE%97%E6%B3%95%E7%BB%83%E4%B9%A0%E7%AC%94%E8%AE%B0.assets/1620.jpeg)

Left = index * 2 + 1

Right = index * 2 + 2

Parent(i) = floor((i-1)/2)

#### 二叉函数展开为链表

后序遍历

https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

#### 二叉搜索树的序列化与反序列化

二叉搜索树的特点：左小右大

https://leetcode.cn/problems/serialize-and-deserialize-bst/

#### 二叉搜索树第k小的元素

https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

二叉搜索树的中序遍历，得到升序数组。

#### 通过中序遍历，后序遍历的数组构建二叉树

https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

通过后续遍历找到当前root，再通过root在中序遍历中找左右子树。递归构建

### 回溯算法

#### 分割回文串

https://leetcode-cn.com/problems/palindrome-partitioning/

模拟一刀一刀地切过程，保证每一次切时，前面的字符是回文串。

#### 迷路的机器人

https://leetcode-cn.com/problems/robot-in-a-grid-lcci/

记录下已经回溯过的点，避免重复探索。

#### 零钱兑换

每次选择一种硬币，path为选择的硬币。

https://leetcode-cn.com/problems/coin-change/

### 深度优先搜索

#### 迷你语法分析器

https://leetcode-cn.com/problems/mini-parser/solution/mi-ni-yu-fa-fen-xi-qi-by-leetcode-soluti-l2ma/

深度优先搜索或者栈。

### 找逆序对，归并排序

https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

左指针每次右移，都计算其“贡献度”。

如果右边全部大于左边，左指针贡献度一直是0

如果有右边的先走了，他会比后来入队的左指针小，每次它都贡献1。

### 



## 广度优先搜索

### 最大人工岛问题

https://leetcode-cn.com/problems/making-a-large-island/

对于每个算出面积的岛屿可以为它打上独一无二的标签，以方便计算后面的面积扩张与避免重复。

## 动态规划

### 最大公共子数组问题

## 贪心算法

### 排布二进制网格的最少交换次数

https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/

### 翻卡片游戏

https://leetcode-cn.com/problems/card-flipping-game/

任何正反面不重复的卡都可能是答案！

### 美化数组中的最小删除数字

https://leetcode-cn.com/problems/minimum-deletions-to-make-array-beautiful/

贪心的思想

## 小trick

### 找到指定长度的回文数

https://leetcode-cn.com/problems/find-palindrome-with-fixed-length/

回文数组可以使用字符串进行构建。

**长度为5的回文数中，第n大的为：100+n-1**

这是解题的关键

### 分类讨论算法：强密码检验器

https://leetcode-cn.com/problems/strong-password-checker/solution/qiang-mi-ma-jian-yan-qi-by-leetcode-solu-4fqx/

困难题

情况1，长度小于6

情况2，长度大于等于6，小于等于20

情况3，大于20

### 分类讨论算法：HTML实体解析器

`&XX; `  匹配这样的字符串，不能从前向后匹配，因为&后面可能没有；也可能有&。但是; 前面匹配唯一一个&。

### 密码验证合格程序：

https://www.nowcoder.com/practice/184edec193864f0985ad2684fbc86841?tpId=37&tqId=21243&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

### 模拟：删除第p个元素

### 如何判断是否为质数

一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。

### 把字母进行二进制编码进行哈希

如何把一个字母编码到一个二进制中？

使用位运算：

```python
bin(1 << (ord('b') - ord('a')))
```

使用数字计算：

```python
i = 0
for char in set(word):
    n = ord(char) - ord("a")
    i += 2 ** n
print(bin(i))
```

### 使用any和all

```
all([1,1,1]) = True
any([1,0,0]) = True
```

如何按列解包：

```python
[col for col in zip(*board)]
```

### 排列组合的计算：数字中各个digit都不同的个数

n=0，1个

n=1, 10个

n=2，91个

n>=2时，假设第一位不用0：

第n位为
$$
9*A_{9}^{n-1}
$$
所以递推公式为：
$$
res =9\times A_{9}^{n}+...+9\times A_{9}^{2}+9\times A_{9}^{1}+10
$$

### 曼哈顿距离：最短路径

https://leetcode-cn.com/problems/escape-the-ghosts/

需要计算多个点到一个target的最短路径，而且这个地图是无限的，没有障碍的。

不要被广度优先算法禁锢住思想，使用**曼哈顿距离**直接计算出最短路径！

### O(1) 时间插入、删除和获取随机元素

为了确保严格 O(1)，我们不能使用**拒绝采样**和在**数组非结尾位置添加/删除元素**

维护一个哈希表；

一个数组，为了方便地修改，我们要方便地找到数的index

hash[num] = index 用这样的哈希表来维护数组。

random.choice()

### 前缀树：键值映射

https://leetcode-cn.com/problems/map-sum-pairs/

```
class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]

```

### 暴力遍历中的缩小搜索空间：最大回文数乘积

https://leetcode-cn.com/problems/largest-palindrome-product/

n位的回文数字，这个范围实际上并不算大，可以暴力遍历。

找公约数的过程要注意减小搜索空间。

### 双向扫描：字符的最短距离

https://leetcode-cn.com/problems/shortest-distance-to-a-character/

问题转化

ans = min(和左边c的距离，和右边c的距离)

假设两个哨兵c

### 文件的最长绝对路径

https://leetcode-cn.com/problems/longest-absolute-file-path/

处理文件字符串的时候，会遇到 \n\t等字符，注意转义。

深度优先搜索可以使用栈。

### 贪心：和为 K 的最少斐波那契数字数目 

https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

贪心算法，斐波那契数增长的很快，不必担心数据大小问题。

### 分治：漂亮数组

https://leetcode-cn.com/problems/beautiful-array/

难在将问题分割为子问题。

### 寻找并简化递归关系：旋转函数

https://leetcode-cn.com/problems/rotate-function/

注意要将递归关系简化成方便计算的形式。

### （未完成）求凸包：安装栅栏

https://leetcode-cn.com/problems/erect-the-fence/solution/an-zhuang-zha-lan-by-leetcode-solution-75s3/

为了便于理解，本次使用 O(n^2)的算法。

首先找到最左边的一个点。

我们要找到“最外侧的点”：

​		比如：最左侧点为A，怎么找到B点是最外侧呢？

​		假定B‘ 点，然后计算其他点R：是否存在R，让B'R 与 AB’ 向量的夹角大于180度？

​		如果存在就说明这个B‘点不合格，R点在更外侧。

如何判断两个向量的夹角大小呢？使用向量叉积。

### 自定义排序，自定义比较规则：重新排列日志文件

https://leetcode-cn.com/problems/reorder-data-in-log-files/

对于需要排序的问题，有些时候有比较优先级，可以自己定义一个比较函数，用于比较。

```python
def func():

	return (priority1,priority2,..,)

sort(key=func)
```

### 队列模拟，约瑟夫环：丢手绢

https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game/

递归，约瑟夫环：

第一次排除第k个人，第二次还是第k个，人的总数从n变为n-1

### 贪心：增减字符串匹配

https://leetcode.cn/problems/di-string-match/

贪心

### 二分查找：搜索二维矩阵 II

定位有序数组，在改数组进行二分。

https://leetcode.cn/problems/search-a-2d-matrix-ii/
