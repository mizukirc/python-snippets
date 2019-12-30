### Documentation:

[bool](https://docs.python.org/ja/3/library/functions.html#bool)  
[ブール値](https://docs.python.org/ja/3/library/stdtypes.html#bltin-boolean-values)
真偽の判定

### Syntax:

```bool([exp])```

- **exp**: 真偽の評価対象となる expression. exp がない場合，既定値としてFalseを返す.

### Returns:

bool

### Example: 

```python
>>> bool(1)
True

>>> bool(0)
False

>>> x = 3
>>> bool(x == 3)
True

>>> bool([])
False
```

### Note:
入力が以下の場合，結果は False となる．
- False
- None
- 数字のゼロ
- 空の文字列，containers (str, tuple, list, dict, set, frozenset) 
