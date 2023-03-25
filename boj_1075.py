import sys
n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

n1 = n//100 * 100
for i in range(f) :
    if (n1+i)%f == 0 :
        print(f'{i:02d}')
        break
