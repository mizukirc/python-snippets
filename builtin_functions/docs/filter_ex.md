### Documentation:

[filter](https://docs.python.org/ja/3/library/functions.html#filter)  


### Syntax:

```filter(func, iter)```

- **func**: iter に対して適用したい関数．None に設定されていれば，True の要素のみを返す
- **iter**: iterable object 

### Returns:

func で定義されている戻り値の形と同様

### Example: 

```python
>>> list(filter(lambda x: x > 3, [-1, 5, 10, 2]))
[5, 10]

# 文字列から数値だけを抽出
>>> S = 'AbCD9876'
>>> filter(lambda j: j % 2 == 0, map(int, [i for i in S if str.isdigit(i)]))
[6, 8]

```

### Note:
```
filter(function, iterable) 
```
はジェネレータ式で表現することができます．第一入力引数の func が None に設定されていれば
```
item for item in iterable if item
```
func が None ではなく関数が設定されていれば，
```
item for item in iterable if function(item)) 
```
と等価です．
