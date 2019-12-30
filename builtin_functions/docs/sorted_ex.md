### Documentation:

[sorted](https://docs.python.org/ja/3/library/functions.html#sorted)  
[ソート HOW TO](https://docs.python.org/ja/3/howto/sorting.html)

### Syntax:

```sorted(a[, key=b, reverse=True])```

- **a** (list): ソート対象となるリスト．

#### Options:
- **key**: ソートをする前に実行する関数．リスト内に tuple/dict などが含まれているときに，どの要素でソートするかなどを指定する．
- **reverse** (bool): 既定は False で，昇順になっている．True にすることで降順の結果を得る．

### Returns:

list

### Example:

```python
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```

### Note:

list.sort() メソッドでも同様ことができる．

```python
>>> a = ['b', 'c', 'a']
>>> a.sort()
>>> a   # a は上書きされる
['a', 'b', 'c']
```
