=====
itertool.permutations()
=====

長さ r の順列 (permutation) の作成

Syntax
======
**permutations(iter[, r=None])**

**iter** 
    配列やセットなどの iterable object
**r**  
    順列の数 (tuple の長さ) 


Returns
============
iterable object

Example
=======
- a の要素の順列 tuple の list を作成 :: python
    >>> from itertools import permutations
    >>> a = [1,2,3]
    >>> list( permutations(a, 2) )
    [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


- a の要素の順列をループ内でインデクス i として使用 :: python
    >>> for i in permutations(a, 2):
    >>>     print(i)
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)

- b の要素をソートし、文字列のみを表示 :: python
    >>> results = ['ABCD']
    >>> num = 2
    >>> results = sorted(permutations(instr, num))
    >>> [print(*x, sep='') for x in results]    
    AC
    AH
    AK
    CA
    CH
    CK
    HA
    HC
    HK
    KA
    KC
    KH

Note
====


See Also
========
- official document
    [itertools.permutations](https://docs.python.org/ja/3/library/itertools.html#itertools.permutations)
