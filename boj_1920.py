import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
for v in b :
    print(1 if v in a else 0)

