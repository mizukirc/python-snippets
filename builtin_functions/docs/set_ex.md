### Documentation:

[set](https://docs.python.org/ja/3/library/functions.html#func-set)  
重複や順番なしの集合の定義

### Syntax:

```set(a)```  

- **a** (list): 集合の作成元リスト

**{ }** でも作成できる．

### Returns:

set

### Example: 

```python
>>> set([1,5,3,6])
{1, 3, 5, 6}

>>> {1,5,3,6}
{1, 3, 5, 6}

>>> set()
set()

>>> {i*2 for i in range(3)}
{0, 2, 4}
```

### Note:
list や tuple に変換するときは list(), tuple() を使用  
[method list](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset)
