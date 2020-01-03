### Documentation:

[dict](https://docs.python.org/ja/3/library/functions.html#func-dict)  
辞書の作成

### Syntax:

```dict([a])```

- **a** (optional): 
**{ }** でも dictionary object を作成可能

### Returns:

dictionary object

### Example: 

```python
>>> phonebook = dict()
>>> for i in range(3):
>>>     entry = input().rstrip().split()
>>>     phonebook[entry[0]] = int(entry[1])
in> sam 1
in> tom 6
in> jim 4
>>> phonebook
{'sam': 1, 'tom': 4, 'jim': 6}

```