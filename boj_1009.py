import sys
n = int(sys.stdin.readline())
answer = []
for _ in range(n) :
    a, b = map(int,sys.stdin.readline().split())
    r = [a%10]
    prev_num = a%10
    while True :
        prev_num = (prev_num*a)%10
        if  prev_num == r[0] :
            break
        else :
            r.append(prev_num)
    answer.append(r[(b-1)%len(r)] if r[(b-1)%len(r)] else 10)

for v in answer :
    print(v)