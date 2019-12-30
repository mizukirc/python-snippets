### Documentation:

[tuple](https://docs.python.org/ja/3/library/functions.html#func-tuple)  
複数の要素で構成される組（異なるデータ型が含まれていてもよい）

### Syntax:

```tuple(a)```

- **a** (list): tuple に変換するリスト．   
**( )** で tuple を作成することも可能．

### Returns:

tuple

### Example: 

```python
>>> tuple([1, 2, 'あいう'])
(1, 2, 'あいう')

>>> (1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)

>>> (1,2,3) + (4,)
(1, 2, 3, 4)

```

### Note:
list は変更可能だが，tuple は変更できない．たとえば以下のような事はできない．

```python
# error - tuple
>>> a = tuple([1, 2, 'あいう'])
>>> a[2] = 4

# pass - list
>>> a = [1, 2, 'あいう']
>> a[2] = 4
>>> a
[1, 2, 4]
```

要素を変更/削除する場合は一度 list に変換して insert() や remove() で対応．
