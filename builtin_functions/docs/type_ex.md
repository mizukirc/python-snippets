### Documentation:

[type](https://docs.python.org/ja/3/library/functions.html#type)  
オブジェクトのデータ型を判定

### Syntax:

```type(obj[, bases, dict])```

- **obj**: 型を確認したい対象オブジェクト  
- **bases** (optional): ベースのクラス  
- **dict** (optional): クラスの名前空間  

### Returns:

type

### Example: 

```python
>> type(6)
int

>> type('6')
str

>> type(True)
bool

>> type({"one":1, "two":2})
dict

>> type(type(1))
type

>> type(print)
builtin_function_or_method

```