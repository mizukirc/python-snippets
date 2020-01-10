### Documentation:

[eval](https://docs.python.org/ja/3/library/functions.html#eval)  
文字列で与えられた式を評価

### Syntax:

```eval(exp[, globals, locals])```

- **exp** (str): 文字列で表記された数式
- **globals** (dict): 実行する namespace を定義した辞書
- **locals** (dict): local namespace に定義された辞書

### Returns:

(式の算出結果)

### Example: 

```python
>>> x = 1
>>> eval('x+1')
2

# 式 P に x を代入した結果を返す
>>> x = 1
>>> P = 'x**3 + x**2 + x + 1'
>>> eval(P, {'x': x})
4

```

