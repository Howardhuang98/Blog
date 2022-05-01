# python logging 标准库

什么时候使用日志？

![image-20220107220250308](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/image-20220107220250308.png)

日志的级别：

* DEBUG(调试级别)
* INFO(信息)
* WARNING(警告)
* ERROR(错误)
* CRITICAL(严重错误)

> 默认情况下只有warning以上才会输出到console。一般来说logging都是多线程的，避免io对主线程的影响。

## logging 的模块化设计

![img](python%20logging%20%E6%A0%87%E5%87%86%E5%BA%93.assets/v2-6e74d55d4a43848e7762a7cad1d27f16_720w.jpg)

四个组件：

- Loggers记录器，相当于笔，用于写log
- Handlers处理器，可以把写好的log发送到目的地，比如email，文本等
- Filter过滤器。（可选）
- Formatters格式化器。（可选）

### Logger

Logger可以在每个文件中获取。

```python
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
```

### Handlers

将日志分发到不同的目的地。

```python
logging.StreamHandler()
logging.RotatingFileHandler()
....
```

### Formatter, Filter (可选)

格式化输出，与过滤输出

```python
logger.addHandler()
logger.addFilter()
```

### 将Logger, Handler, Formatter 连接

```python
handler.setFormatter(formatter)
logger.addHandler(ch)
```

## 实际使用

对于大型项目，最好使用config文件的形式进行配置，但是对于中小型项目，使用脚本进行配置就好。

创建一个log.py文件，在里面定义所有的logger与Handler等组件。

```pyhton
-package
	-module1
	-module2
	-log.py
```

在其他的模块中，直接导入组装好的logger即可

```python
from .log import your_logger
your_logger.debug("Test")
```

log.py文件简易模板：

```python
import logging
import os
from logging.handlers import RotatingFileHandler

os.makedirs('.logs', exist_ok=True)
your_logger = logging.getLogger('bnsl')
your_logger.setLevel(logging.INFO)

fh = RotatingFileHandler(os.path.join('.logs', 'log'), maxBytes=5 * 1024 * 1024, backupCount=10, encoding='utf-8')

f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(f)
your_logger.addHandler(fh)
```

