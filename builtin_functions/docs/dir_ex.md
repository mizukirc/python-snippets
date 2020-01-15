### Documentation:

[dir](https://docs.python.org/ja/3/library/functions.html#dir)  
モジュールで定義されている名前（関数，変数など）一覧の表示

### Syntax:

```dir([obj])```

- **obj**: 属性を表示したいオブジェクト．空の場合はローカルスコープにある名前リストを表示．

### Returns:

str の list （アルファベット順）

### Example: 

```python
>>> dir()
# 現在定義されている名前が表示される

>>> dir(__builtins__)
# 組み込みの関数や変数の名前が表示される

>>> dir(list)
# list 型が持つ名前が表示される
```


### Note:
[help](https://docs.python.org/ja/3/library/functions.html#help)でも名前一覧を表示することができる．



