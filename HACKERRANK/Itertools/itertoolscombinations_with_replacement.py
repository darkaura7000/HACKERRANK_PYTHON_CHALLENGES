"""

Problem   : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""
from itertools import *

s, n = input().split()
n = int(n)
s = sorted(s)
for j in combinations_with_replacement(s, n):
    print("".join(j))
