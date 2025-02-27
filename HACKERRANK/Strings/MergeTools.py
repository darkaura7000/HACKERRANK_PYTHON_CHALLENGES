'''

Problem   : https://www.hackerrank.com/challenges/merge-the-tools/
'''
from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0, len(string)-k+1, k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
