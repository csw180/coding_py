# 백준 알파벳 다이아몬드 https://www.acmicpc.net/problem/1262

import sys
import string

def distance(r,c,center_r, center_c) :
    return abs(r-center_r) + abs(c-center_c)

n,r1,c1,r2,c2 = map(int,sys.stdin.readline().split(' '))
alpha =  string.ascii_lowercase

r,c  = n-1,n-1
for i in range(r1,r2+1) :
    tmp_str = ''
    for j in range(c1,c2+1):
        dstns = distance(i%(2*n-1),j%(2*n-1),r,c)
        tmp_str += alpha[dstns%26] if dstns < n  else '.'
    print(tmp_str)
