### Documentation:

[len](https://docs.python.org/ja/3/library/functions.html#len)  
オブジェクトの長さ

### Syntax:

```len(a)```

- **a**: 長さを取得する対象の sequence or collection 

sequence: str, tuple, range, list, ...  
collection: dict, set, frozenset, ...

### Returns:

int

### Example: 

```python
>>> len([1, 2, 3])
3

>>> len({'one':1, 'two':2})
2

>>> len([])
0
```

### Note:
入力が数値 (int/float) の場合はエラーになる．
例えば以下のような例はNG.
```python
>>> len(5)
```

