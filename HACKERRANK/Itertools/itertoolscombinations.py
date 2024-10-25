"""

Problem   : https://www.hackerrank.com/challenges/itertools-combinations/problem
"""
from itertools import *

s, n = input().split()
n = int(n) + 1
s = sorted(s)
for i in range(1, n):
    for j in combinations(s, i):
        print("".join(j))
