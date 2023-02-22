from collections import Counter
def solution(weights):
    d = dict()
    for i,w in enumerate(weights) :
        for m in [2,3,4] :
            if d.get(w*m) is None :
                d[w*m] = 0
            d[w*m] += 1

    # weight 가 같으면 한번만 count 되어야 하지만 2,3,4 각마디마디
    # 총 3번 count 되기 때문에 weight가 동일한 쌍의 갯수*2 만큼 전체갯수에서 
    # 빼줘야 한다
    c = Counter(weights)
    minus_count = sum(map(lambda x:x[1]*(x[1]-1),filter(lambda x : x[1]>1, c.items())))

    return sum(map(lambda x: x[1]*(x[1]-1)//2 ,d.items())) - minus_count

print(solution([100,180,360,100,270]))
print(solution([100, 100, 100, 200, 200, 200]))


