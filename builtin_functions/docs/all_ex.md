### Documentation:

[all](https://docs.python.org/ja/3/library/functions.html#all)  
対象の配列やセット内のすべての要素が条件を満たす (True) かどうかを判定

### Syntax:

```all(iter)```

- **iter**: 配列やセットなどの iterable object

### Returns:

bool

### Example: 

```python
# True が一つでもあれば True を返す
>>> all([True, False])
False

>>> all([False, False])
False

>>> all([])
True

```






