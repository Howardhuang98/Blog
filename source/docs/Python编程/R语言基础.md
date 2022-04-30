# R语言基础

R语言虽然是基于面向对象开发的，但是其是为数学工作者设计的，所以是一个偏指令型语言。

## 赋值

左右箭头和等号都是支持的。

变量名可以带`.`比如说`var.name`。

```R
a <- 123
b <- 456
print(a + b)
a = 123
b = 456
print(a + b)
```

## 数据类型

数字，字符串，布尔等，R语言都具备。

重要提醒：R的从1开始索引。

额外的，它还具备一些数学方面的数据结构：

### 向量

```R
a = c(3, 4)
a = c(10, 20, 30, 40, 50)
```

### 矩阵

```R
> vector=c(1, 2, 3, 4, 5, 6)
> matrix(vector, 2, 3)
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
```

### array

```R
# 创建两个不同长度的向量
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)

# 创建数组
result <- array(c(vector1,vector2),dim = c(3,3,2))
print(result)
```

### dataframe

```R
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
)
print(table) # 查看 table 数据
```

### factor

```R
x <- c("男", "女", "男", "男",  "女")
sex <- factor(x)
print(sex)
print(is.factor(sex))
```

## 逻辑操作

### if 语句

```R
if(boolean_expression) {
    // 布尔表达式为真将执行的语句
}
```

### while 语句

```R
while(condition)
{
   statement(s);
}
```

### for 语句

```R
for (value in vector) {
    statements
}
```

## 使用包package

```
library("包名")
```

