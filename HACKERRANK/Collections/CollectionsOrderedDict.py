"""

Problem   : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

import collections
import re

n = int(input())
item_od = collections.OrderedDict()
for _ in range(n):
    record_list = re.split(r"(\d+)$", input().strip())
    item_name = record_list[0]
    item_price = int(record_list[1])
    if item_name not in item_od:
        item_od[item_name] = item_price
    else:
        item_od[item_name] = item_od[item_name] + item_price
for i in item_od:
    print(f"{i}{item_od[i]}")
