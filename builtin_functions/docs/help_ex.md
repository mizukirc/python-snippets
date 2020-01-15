### Documentation:

[help](https://docs.python.org/ja/3/library/functions.html#help)  
ヘルプの表示

### Syntax:

```help([obj])```

- **obj**: ヘルプを表示したいオブジェクト．空の場合はヘルプガイドが表示される．入力引数が文字列の場合、モジュール，関数，クラス，メソッド，キーワード，トピックを検索し，該当するヘルプページを表示する．入力引数が文字列以外の場合，その変数の型のヘルプを表示する．

### Returns:

(ヘルプの表示)

### Example: 

```python
>>> help()
# インタラクティブなヘルプガイドが表示される

>>> help(dir)
# dir() のヘルプが表示される

>>> help('tensorflow')
# TensorFlow のヘルプが表示される

```

### Note:
[pydoc](https://docs.python.org/ja/3/library/pydoc.html#module-pydoc) でヘルプページを作成することができる．




