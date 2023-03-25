import sys
for _ in range(3) :
    n = int(sys.stdin.readline())
    sum = 0
    for _ in range(n) :
        v = int(sys.stdin.readline())
        sum += v
    print("0" if sum==0 else ( "+" if sum > 0 else "-"))
