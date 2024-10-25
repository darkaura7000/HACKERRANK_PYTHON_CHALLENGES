"""

Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""

n = input()
ar = input().split()
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))
