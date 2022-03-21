# try的用法

## python的异常：

程序在运行的时候，如果python解释器遇到一个错误，会停止程序的执行，并且提示一些错误的信息，这就是异常。

在程序开发中，如果对某些代码能否执行不确定，可以增加try来捕获异常

try: 尝试执行代码

except: 出现错误的处理

```
while True:
    try:
        x = int(input("请输入一个int："))
        break
    except ValueError:
        print("发生了ValueError，请重试")
```

[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句的工作原理如下：

- 首先，执行 *try 子句* （[`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 和 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 关键字之间的（多行）语句）。
- 如果没有异常发生，则跳过 *except 子句* 并完成 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句的执行。
- 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 然后，如果异常的类型和 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 关键字后面的异常匹配，则执行 except 子句，然后继续执行 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句之后的代码。
- 如果发生的异常和 except 子句中指定的异常不匹配，则将其传递到外部的 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句中；如果没有找到处理程序，则它是一个 *未处理异常*，执行将停止并显示如上所示的消息。

## python的语法错误

Syntax Error: invalid syntax

