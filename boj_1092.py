# https://www.acmicpc.net/problem/1092
# 배

import sys
n = int(sys.stdin.readline())
cranes = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int,sys.stdin.readline().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
if  cranes[0] < boxes[0] :
    print(-1)
    exit()

repeat = 0
while  boxes:
    repeat += 1

    for crane in cranes :
        for box in boxes :
            if  crane >= box :
                boxes.remove(box)
                break
    
print(repeat)
