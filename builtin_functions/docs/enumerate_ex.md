### Documentation:

[enumerate](https://docs.python.org/ja/3/library/functions.html#enumerate)  
オブジェクトの長さ

### Syntax:

```enumerate(seq[, startidx])```

- **seq**: sequence/iterator
- **startidx** (int): 開始インデクス番号 

### Returns:

enumerate object

### Example: 

```python
>>> a = [4,8,2]
>>> list(enumerate(a))
[(0, 4), (1, 8), (2, 2)]

>>> for i, val in enumerate(a):
>>>     print(i, val)
0 4
1 8
2 2

>>> for i, val in enumerate(a, start=5):
>>>     print(i, val)
5 4
6 8
7 2

```



