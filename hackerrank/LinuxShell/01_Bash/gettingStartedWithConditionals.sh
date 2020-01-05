#!/bin/bash
# https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/

read str

if [ $str == 'y' -o $str  == 'Y' ] ; then
    echo 'YES'
elif [ $str == 'n' -o $str == 'N' ] ; then
    echo 'NO'
fi

