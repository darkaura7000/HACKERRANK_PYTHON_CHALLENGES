"""

Problem   : https://www.hackerrank.com/challenges/incorrect-regex/problem
"""

import re

n = int(input())
for _ in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except Exception as e:
        print(False)
