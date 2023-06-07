# 백준 기타리스트 : 1495 https://www.acmicpc.net/problem/1495

import sys

def addsublist(a, lst, limit) :
    """
    list(lst) 의 각 요소를 대상으로 a  를 더하거나 빼서 나온값중에서
    0~limit 사이값만 리턴하는 함수
    """
    result_set = set()
    for v in lst :
        if v + a <= limit :
            result_set.add(v + a)
        if v - a >= 0 :
            result_set.add(v - a)
    return list(result_set)

input = sys.stdin.readline
n,s,m = map(int,input().split())
volumes = list(map(int,input().split()))

dplist = [s]
for  volume in volumes :
    dplist = addsublist(volume, dplist, m)

print(max(dplist) if dplist else -1)