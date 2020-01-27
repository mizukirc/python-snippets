=====
itertool.groupby()
=====

連続した key とそのグループの要素を返す

Syntax
======
**groupby(iter[, key=None])**

**iter** 
    配列やセットなどの iterable object
**key**  
    各要素の key 値を算出する関数


Returns
============

iterable object

Example
=======
- 0 と 1 のリストから，0/1 をキー，それぞれの集まりを group として抽出 :: python
    >>> from itertools import groupby
    >>> binary_lst = [1,0,1,0,0,0,1]
    >>> gr = groupby(binary_lst)
    >>> for key, group in gr:
    >>>     print(key, list(group))
    1 [1]
    0 [0]
    1 [1]
    0 [0, 0, 0]
    1 [1]

Note
====


See Also
========
- official document
    [itertools.groupby](https://docs.python.org/3.8/library/itertools.html#itertools.groupby)
