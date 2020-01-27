=====
collections.Counter()
=====

各要素の出現回数をカウント

Syntax
======
**Counter([iter_or_map])**

**iter_or_map** 
    配列やセットなどの iterable object あるいは map object

Returns
============

Counter object (dict subclass)

Example
=======
- リスト内のユニークな要素の数をカウントし，dict で返す．各要素の数は要素名で参照することが可能． :: python
    >>> from collections import Counter
    >>> a = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    >>> c = Counter(a)
    >>> print(c)
    Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})
    >>> c[5]
    2

- 入力引数は空でも Counter object を作成可能 :: python
    >>> c = Counter()
    >>> c
    Counter()

Note
====


See Also
========
- official document
    `collections.Counter <https://docs.python.org/3/library/collections.html#collections.Counter>`_
