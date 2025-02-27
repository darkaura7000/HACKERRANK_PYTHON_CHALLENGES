"""

Problem   : https://www.hackerrank.com/challenges/python-time-delta/problem
"""

import datetime

cas = int(input())
time_format = "%a %d %b %Y %H:%M:%S %z"
for _ in range(cas):
    timestamp1 = input().strip()
    timestamp2 = input().strip()
    time_second1 = datetime.datetime.strptime(timestamp1, time_format)
    time_second2 = datetime.datetime.strptime(timestamp2, time_format)
    print(int(abs((time_second1 - time_second2).total_seconds())))
