# https://www.acmicpc.net/problem/1259
# 팰린드롬수

import sys

result = ''
while True :
    n = sys.stdin.readline().strip()
    if n=='0' :
        break
    if n==n[::-1] :
        result = 'yes'
    else :
        result = 'no'
    print(result)
