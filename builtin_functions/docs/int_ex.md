### Documentation:

[int](https://docs.python.org/ja/3/library/functions.html#int)  
数値あるいは文字列を整数型に変換

### Syntax:

```int([a])```
```int(a, base=b)```
```int(a, b)```

- **a** (optional): 数値あるいは文字列．規定値は0．


#### Options:
- ***base***: 基数を指定．
- **b**: 基数．0, あるいは 2から36 の数値で指定可能．

### Returns:

int

### Example: 

```python
>> int(3.14)
3

>> int('56')
56

>> int('1101', 2)
13
```
