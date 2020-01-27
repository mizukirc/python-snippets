=====
itertool.permutations()
=====

長さ r の順列 (permutation) の作成

Syntax
======
**permutations** *(iter[, r=None])*

*iter*  
    配列やセットなどの iterable object
*r*  
    組み合わせの数 (tuple の長さ) 


Returns
============
iterable object

Example
=======
- a の要素の組み合わせ tuple の list を作成 :: python
    >>> a = [1,2,3]
    >>> list( permutations(a, 2) )
    [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


- a の要素の組み合わせをループ内でインデクス i として使用 :: python
    >>> for i in permutations(a, 2):
    >>>     print(i)
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)

Note
====


See Also
========
