### Documentation:

[min](https://docs.python.org/ja/3/library/functions.html#min)  
配列の最小値

### Syntax:

```min(a)```

- **a**: collection (list/iterable sequence)

### Returns:

(入力の中の最小となる値)

### Example: 

```python
>>> min(1, 3, 2)
1

# アルファベット順
>>> min('one', 'two', 'three')
'one'

# key を基準とした最小値
>>> max('one', 'two', 'three', key=len)
'one'

# 辞書のキー (key) の最小値
>>> d = {'a': 80, 'b': 120, 'c': 110}
>>> min(d)
'a'

# 辞書の値 (value) の最小値
>>> min(d.values())
80

# 辞書の値が最小となるキーの取得
>>> min(d, key=d.get)
'a'

# 辞書の値が最小となるキーと値の取得
>>> min(d.items(), key=lambda x:x[1])
('a', 80)
```

