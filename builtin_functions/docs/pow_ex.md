### Documentation:

[pow](https://docs.python.org/ja/3/library/functions.html#pow)  
数値のべき乗

### Syntax:

```pow(base, exp[, mod])```

- **base** (int/float): べき乗の基数
- **exp** (int/float): べき乗の指数
- **mod**: $pow(base, exp) % mod$ の計算

### Returns:

int/float

### Example: 

```python
>>> pow(67, 7, 5)
3
>>> pow(67, 7) % 5
3
```

### Note:
