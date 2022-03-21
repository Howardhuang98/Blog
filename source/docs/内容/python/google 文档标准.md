# Google 文档标准

Python 使用*文档字符串*来记录代码。文档字符串是一个字符串，它是包、模块、类或函数中的第一条语句。这些字符串可以通过`__doc__`对象的成员自动提取出来。

## 模块

每个文件都应包含许可证样板。为项目使用的许可证选择适当的样板（例如，Apache 2.0、BSD、LGPL、GPL）

文件应以描述模块内容和用法的文档字符串开头。

```
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

## 函数和方法



```python
def fetch_smalltable_rows(table_handle: smalltable.Table,
                          keys: Sequence[Union[bytes, str]],
                          require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str, ...]]:
    """Fetches rows from a Smalltable.Retrieves rows pertaining to the given keys from the Table instance
represented by table_handle.  String keys will be UTF-8 encoded.

Args:
    table_handle: An open smalltable.Table instance.
    keys: A sequence of strings representing the key of each table
      row to fetch.  String keys will be UTF-8 encoded.
    require_all_keys: If True only rows with values set for all keys will be
      returned.

Returns:
    A dict mapping keys to the corresponding table row data
    fetched. Each row is represented as a tuple of strings. For
    example:

    {b'Serak': ('Rigel VII', 'Preparer'),
     b'Zim': ('Irk', 'Invader'),
     b'Lrrr': ('Omicron Persei 8', 'Emperor')}

    Returned keys are always bytes.  If a key from the keys argument is
    missing from the dictionary, then that row was not found in the
    table (and require_all_keys must have been False).

Raises:
    IOError: An error occurred accessing the smalltable.
"""
```

## 类

```python
class SampleClass:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

