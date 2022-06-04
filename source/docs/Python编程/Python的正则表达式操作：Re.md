# Python的正则表达式操作：Re

## 总览

正则表达式代表了**一系列字符串**；

正则表达式中有一些特殊定义的字符，在这里介绍常用的字符:

- `*` 对前面的正则式匹配0到任意次；
- `+`对前面的正则式匹配1到任意次；
- `?`对前面匹配0，1次；
- `{m,n}` 对前面的表达式匹配m到n次；
- `.` (点) 在默认模式，匹配除了换行的任意字符；
- `[]`一个字符集合，例如`[a,b,c]`；
- `()`将正则表达组合；
- `\`转义特殊字符，一般用在 `\+` `\.` `\*`；



## 正则表达式对象 Pattern

Pattern实际上可以是一个字符串（正则表达式）；也可以是一个Pattern对象，方便后期的管理。

`re.search(pattern, string, flags=0*)` 找到匹配样式的**第一个**位置，返回相应的`Match`对象

`re.match(pattern, string, flags=0*)`找到匹配样式的**一个或多个**，返回相应的`Match`对象

`re.sub(pattern,repl,string)`使用`repl`代替`string`中的匹配到pattern的子字符串

都可以使用Pattern来实现：

`Pattern.search(string)`

`Pattern.match(string)`

## 匹配对象 Match

匹配可能不止一个：

`Match.groups()`

`Match[g]`