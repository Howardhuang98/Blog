# SPHINX 使用

文档结构

```
docs
├── build
├── make.bat
├── Makefile
└── source
   ├── conf.py
   ├── index.rst
   ├── _static
   └── _templates
```

build 渲染后的结果页面

makefile

source/conf.py 

source/index.rst 主页，必须包含 table of contents tree，*toctree*，包含所有页面

## build

写好了以上就可以build，它会将生成好的html文件放入到/build文件目录下

## extensions 扩展

扩展写在conf.py内，可以添加。

```python
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
```

## 主题

要在环境中安装"pip"  主题

再修改conf文件

## 描述符

代码块

.. code-block:: console

