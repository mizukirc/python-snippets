### Documentation:

[any](https://docs.python.org/ja/3/library/functions.html#any)  
対象の配列やセット内に条件を満たす要素 (True) があるかどうかを判定

### Syntax:

```any(iter)```

- **iter**: 配列やセットなどの iterable object

### Returns:

bool

### Example: 

```python
# True が一つでもあれば True を返す
>>> any([True, False])
True

>>> any([False, False])
False

>>> any([])
False

```






