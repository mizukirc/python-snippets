=====
itertool.combinations()
=====

長さ r の組み合わせ (combination) の作成

Syntax
======
**combinations(iter[, r=None])**

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
    >>> from itertools import combinations
    >>> a = [1,2,3]
    >>> list( combinations(a, 2) )
    [(1, 2), (1, 3), (2, 3)]


- a の要素の組み合わせをループ内でインデクス i として使用 :: python
    >>> for i in combinations(a, 2):
    >>>     print(i)
    (1, 2)
    (1, 3)
    (2, 3)

- b の要素をソートし、文字列のみを表示 :: python
    >>> results = ['ABCD']
    >>> num = 2
    >>> results = sorted(combinations(instr, num))
    >>> [print(*x, sep='') for x in results]    
    AC
    AH
    AK
    CH
    CK
    HK    

Note
====
permutations は重複を許すが，combinations は重複なし

See Also
========
- official document
    [itertools.combinations](https://docs.python.org/ja/3/library/itertools.html#itertools.combinations)
