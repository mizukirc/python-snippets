### Documentation:

[zip](https://docs.python.org/ja/3/library/functions.html#zip)  


### Syntax:

```zip([iterable])```

- **iterable**: iterable object

### Returns:

zipped object, containing tuples of original iterable objects

### Example: 

```python
>>> zip()
[]

>>> out_a, out_b = zip(['a', 'b'], [1, 2])
>>> print(out_a, out_b, sep=' ')
('a', 1) ('b', 2)

>>> out_a = list(zip('abc', '123'))
>>> print(out_a)
[('a', '1'), ('b', '2'), ('c', '3')]

>>> out_a = zip((1, 2, 3), (4, 5))
>>> print(*out_a)
(1, 4) (2, 5)
```

