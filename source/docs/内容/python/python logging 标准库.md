# python logging 标准库

什么时候使用日志？

![image-20220107220250308](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/image-20220107220250308.png)

日志的级别：

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

默认情况下会将logging输出到命令行（console），默认的输出级别为warning。

```python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
```

## 输出日志到文件

```python
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
```

## 从多个模块记录日志

![image-20220107220743947](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/image-20220107220743947.png)

在这种情况下，mylib.py中的产生的日志信息也被记录下来放在了一个log文件中。**不同模块的日志被统一记录，无法区分日志的来源**。

## 日志库的组件：

* 记录器

* 处理器

* 过滤器

* 格式器

![A guide to logging in Python | Opensource.com](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/4-nfjk7uc.jpg)

![img](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/v2-6e74d55d4a43848e7762a7cad1d27f16_720w.jpg)

### Logger

记录器，它主要负责两个功能：

1. 配置
2. 消息

**配置**常用`Logger.setLevel()`来指定处理的最低严重性日志消息。

`Logger.addHandler()`

`Logger.addFilter()`

消息常用

`Logger.debug()`,` Logger.info()` 

### Handler 

两个常用的处理器为

`StreamHandler`, `FileHandler`

## 实践

在实际使用中，如果是小型项目，可以显式地创建记录器，处理器等。

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

大型项目可能涉及到多个记录器处理器，所以在config文件中统一配置：

logging.conf

```python
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

模块中使用

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

