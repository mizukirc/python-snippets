### Documentation:

[range](https://docs.python.org/ja/3/library/functions.html#func-range)  
数値の配列を作成

### Syntax:

```range([a,] b [, c])```

- **a** (int, optional): sequence の開始点．数値 a は結果に含まれる．既定値は0．  
- **b** (int): sequence の上限．数値 b は結果に含まれない．  　　
- **c** (int, optional): sequence の間隔．既定値は1．　  　

### Returns:

range object

### Example: 

```python
# run a loop from 3 to 9 with interval of 2
>> for i in range(3,10,2):
>>     print(i, end=', ')
3, 5, 7, 9,

# run a loop from 2 to 4
>> for i in range(2,5):
>>     print(i, end=', ')
2, 3, 4,

# run a loop from 0 to 4
>> for i in range(5):
>>     print(i, end=', ')
0, 1, 2, 3, 4,

```
