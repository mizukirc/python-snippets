=====
itertool.combinations_with_replacement()
=====

長さ r の重複ありの組み合わせ (combination) の作成

Syntax
======
**combinations(iter[, r])**

**iter** 
    配列やセットなどの iterable object
**r**  
    組み合わせの数 (tuple の長さ) 


Returns
============

iterable object

Example
=======
- a の要素の組み合わせ tuple の list を作成 :: python
    >>> from itertools import combinations_with_replacement
    >>> a = [1,2,3]
    >>> list( combinations_with_replacement(a, 2) )
    [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

- a の要素の組み合わせをループ内でインデクス i として使用 :: python
    >>> for i in combinations_with_replacement(a, 2):
    >>>     print(i)
    (1, 1)
    (1, 2)
    (1, 3)
    (2, 2)
    (2, 3)
    (3, 3)

- b の要素をソートし、文字列のみを表示 :: python
    >>> results = ['ABCD']
    >>> num = 2
    >>> results = sorted(combinations_with_replacement(instr, num))
    >>> [print(*x, sep='') for x in results]    
    AA
    AC
    AK
    CC
    CK
    HA
    HC
    HH
    HK
    KK  

Note
====
combinations_with_replacement は重複を許すが，combinations は重複なし．
返り値は iterable object で、list() を実行することで中身を見ることができる．
結果は tuple になっている．


See Also
========
- official document
    `itertools.combinations_with_replacement <https://docs.python.org/3.8/library/itertools.html#itertools.combinations_with_replacement>`_
