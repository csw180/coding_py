import sys

def toggle(A,r,c) :
    for i in range(r,r+3) :
        for j in range(c,c+3) :
            A[i][j] = '1' if A[i][j] == '0' else '0'

n,m = map(int,sys.stdin.readline().split(' '))

A = []
B = []
for i in range(n) :
    A.append(list(sys.stdin.readline().strip()))
for i in range(n) :
    B.append(list(sys.stdin.readline().strip()))

count = 0
for i in range(n-2) :
    for j in range(m-2) :
        if A[i][j] != B[i][j] :
            toggle(A,i,j)
            count += 1
        if A==B :
            break_flag = True
            break
    if A==B :
        break            
if A!= B :
    print(-1)
else :
    print(count)