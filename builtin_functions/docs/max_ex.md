### Documentation:

[max](https://docs.python.org/ja/3/library/functions.html#max)  
配列の最大値

### Syntax:

```max(a)```

- **a**: collection (list/iterable sequence)

### Returns:

(入力の中の最大となる値)

### Example: 

```python
>>> max(1, 3, 2)
3

# アルファベット順
>>> max('one', 'two', 'three')
'two'

# key を基準とした最大値
>>> max('one', 'two', 'three', key=len)
'three'

# 辞書のキー (key) の最大値
>>> d = {'a': 80, 'b': 120, 'c': 110}
>>> max(d)
'c'

# 辞書の値 (value) の最大値 
>>> max(d.values())
120

# 辞書の値が最大となるキーの取得
>>> max(d, key=d.get)
'b'

# 辞書の値が最大となるキーと値の取得
>>> max(d.items(), key=lambda x:x[1])
('b', 120)
```

