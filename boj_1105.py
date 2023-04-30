import sys

L, R = sys.stdin.readline().rstrip().split(' ')
if len(L) != len(R) :
    print(0)
else :
    answer = 0
    for i in range(len(L)) :
        if L[i] != R[i] :
            break
        if L[i] == '8' : answer += 1
    print(answer)
