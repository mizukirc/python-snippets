=====
itertool.product()
=====

リストの直積（デカルト積）を計算

Syntax
======
**product(iter[, repeat])** 

**repeat**: 繰り返し回数

Returns
============

iterable object

Example
=======
- *** :: python
リストの要素ごとに tuple を作成 :: python
    >>> from itertools import product
    >>> l1 = ['A', 'b', 'C']
    >>> l2 = [1, 2, 3]
    >>> list(product(l1, l2))
    [('A', 1),
    ('A', 2),
    ('A', 3),
    ('b', 1),
    ('b', 2),
    ('b', 3),
    ('C', 1),
    ('C', 2),
    ('C', 3)]    

- repeat オプションを設定し、複数回繰り返した tuple を作成 :: python
    >>> l4 = ['a', 'b']
    >>> l5 = ['c', 'd']
    >>> list(product(l2, l3, repeat=2))


Note
====


See Also
========
- official document
    [itertools.product](https://docs.python.org/ja/3/library/itertools.html#itertools.product)
    
