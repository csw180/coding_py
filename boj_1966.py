'''
1966 프린터 큐
https://solved.ac/class/2
큐에 먼저 들어온것을 먼저 프린트 하는것이 아니라
큐에 가장 중요도가 높은것을 프린트하고 나머지는 큐의 맨뒤로 
보내는 방식으로 프린트 한다.
'''
import sys

cases  = int(sys.stdin.readline())
for _ in range(cases) :
    n, s  = map(int,sys.stdin.readline().split(' '))
    nums = list(map(int,sys.stdin.readline().split(' ')))
    slist = [True if i==s  else False for i in range(n) ]

    answer = 0
    while True :
        max_nums = max(nums)
        while nums and nums[0] != max_nums :
            nums.append(nums.pop(0))
            slist.append(slist.pop(0))

        answer += 1
        if  slist[0] :
            print(answer)
            break
        else :
            nums.pop(0)
            slist.pop(0)
        # print(f'{nums}, {slist=}, {answer}')