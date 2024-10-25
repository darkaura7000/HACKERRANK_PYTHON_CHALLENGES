"""

Problem   : https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""

from re import compile, match

pattern = compile("^[-+]?\d*\.\d+$")
for _ in range(int(input())):
    print(bool(pattern.match(input())))
