def solution(cards):
    groups = []
    poss = [i+1 for i in range(len(cards))]
    while(len(poss)>0) :
        pos=poss[0]
        group=[]
        while(cards[pos-1] not in group) :
            group.append(cards[pos-1])
            # print(f'poss remove:{pos}')
            poss.remove(pos)
            pos = cards[pos-1]
        groups.append(group)
        # print(f'groups={groups},poss={poss}')
    answer = sorted(map(lambda x : len(x),groups),reverse=True)
    return answer[0]* (answer[1] if len(answer) > 1 else 0)

print(solution([8,6,3,7,2,5,1,4]))
print(solution([ 2, 3, 4, 5, 6, 7, 8, 9, 10 , 1 ] ))

