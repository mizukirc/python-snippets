### Documentation:

[print](https://docs.python.org/ja/3/library/functions.html#print)  
オブジェクトの値の表示

### Syntax:

```print([obj, sep='', end='n', file=sys.stdout, flus=False])```

- **obj**: sequence/iterator

keywords: 
- **sep** (str): 区切り文字．既定は半角スペース
- **end** (str): 最後に追加する文字．既定はなし
- **file**: 出力するファイル名．既定は sys.stdout
- **flush** (bool): バッファリングしている結果をすべて強制的に出力．ループなどで一度に表示させたくないときに使用．Python 3.3以降のみ対応

### Returns:

None 

### Example: 

```python
>>> print(1, 'a', 2, sep=',')
1,a,2

>>> print(1, 'a', 2, end='!')
1 a 2!

>>> filename = 'test.txt'
>>> print('あいうえお', file = open(filename, "w"))
# test.txt 内に あいうえお が書かれる。

>>> num = 3
>>> print('Array is sorted in %d swaps.' % num)
Array is sorted in 3 swaps.

>>> l = [1,2,3]
>>> print(*l, sep="|")
1|2|3
```



