### Documentation:

[float](https://docs.python.org/ja/3/library/functions.html#float)  
数値あるいは文字列を浮動小数点数型に変換

### Syntax:

```float([a])```

- **a** (optional): 数値あるいは文字列．規定値は0．

### Returns:

float

### Example: 

```python
>>> float(3)
3.0

>>> float('.689')
0.689

>>> float(5.23e-3)
0.00523

>>> float('１２.３４')
12.34

>>> float('Inf')
inf

>>> float('NaN')
nan

>>> float()
0.0

```