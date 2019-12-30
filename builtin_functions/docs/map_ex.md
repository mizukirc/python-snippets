### Documentation:

[map](https://docs.python.org/ja/3/library/functions.html#map)  
list/tuple/dict などの配列に対する関数処理を実施

### Syntax:

```map(func, a)```

- **func**: 関数  
- **a**: 関数に入力する変数 (iterator)  

### Returns:

map

### Example: 

```python
def multiply(x):
    return x*2

>> l = [1, 2, 3]
>> list(map(multiply, l))
[2, 4, 6]

# lambda - 無名関数 
# syntax:
#   lambda 入力引数:出力引数, 入力変数
>> list(map(lambda x:x*2, l))
[2, 4, 6]

>> func = lambda x:x*2
>> list(map(func, l))
[2, 4, 6]

```
