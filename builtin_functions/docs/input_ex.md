### Documentation:

[input](https://docs.python.org/ja/3/library/functions.html#input)  
キーボード入力を取得

### Syntax:

```input()```

### Returns:

str

### Example: 

```python
# get an integer input 
>>> n = int(input())

# 複数の入力がスペースで区切られて入力される場合， split() で出力も分割できる
# map() を使用すると，list object に対して関数を適用でき，以下の例では
# str を int に変換している．
>>> x, k = map(int, input().split())
>>> print(x, k, sep=' ')
# input: 1 2
1 2

```