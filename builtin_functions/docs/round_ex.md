### Documentation:

[round](https://docs.python.org/ja/3/library/functions.html#round)  
小数や整数を任意の桁数で丸める（四捨五入ではなく偶数への丸め）

### Syntax:

```round(num[, digit])```

- **num** (int/float): 丸める対象の数値
- **digit** (int): 丸める桁数

### Returns:

int/float (入力が float で第２引数を指定した場合 float を返す)

### Example: 

```python
>>> num = 123.456
>>> round(num)
123

>>> round(num, -2)
100.0

>>> round(num, 2)
123.457
```

### Note: 
小数を浮動小数点数で正確に表せず，丸め対象の桁の数値が5でも切り捨てられる場合がある．  
詳細は，ドキュメントの [浮動小数点演算，その問題と制限](https://docs.python.org/ja/3/tutorial/floatingpoint.html#tut-fp-issues) を参照．
```python
>>> num = 3.675
>>> round(num,2)
3.67
```