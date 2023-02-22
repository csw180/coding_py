
def solution(scores):
    target=scores[0]
    target_sum =scores[0][0] + scores[0][1]
    scores.sort(key=lambda x : (-x[0],x[1]))

    _max =[scores[0][0],0]
    skiped_scores = []
    for i in range(len(scores)) :
        if  scores[i][0] < _max[0] and scores[i][1] < _max[1] :
            continue
        else :
            skiped_scores.append(scores[i])
            _max[1] = scores[i][1]

    # print(f'skiped_scores={skiped_scores}')
    over_list = list(filter(lambda x : x[0]+x[1] > target_sum,skiped_scores))
    # print(f'over_list={over_list}')
    return  len(over_list)+1 if target in skiped_scores else -1


print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
print(solution([[2,2],[1,4],[3,3],[5,4],[4,1],[3,2],[2,1]]))
