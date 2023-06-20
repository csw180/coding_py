# 백준 문자열교환 : 1522 https://www.acmicpc.net/problem/1522

import sys
input = sys.stdin.readline

string = input().rstrip()
a_count = string.count('a')
len_a = len(string)
string += string
result = []
for i in range(len_a):
    result.append(string[i:i+a_count].count('b'))

print(f'{min(result)}')

