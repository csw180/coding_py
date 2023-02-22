from itertools import combinations

def solution(number):
    c = list(combinations(number,3))
    f = list(filter(lambda x : x==0,map(lambda x : sum(x),c)))
    print(c)
    print(f)
    return len(f)

print(solution([-2, 3, 0, 2, -5]))