
def solution(n, m, section):
    start = section.pop(0)
    paint = 1 
    while section :
        if (start + m) > section[0] :
            section.pop(0)
        else :
            start = section.pop(0)
            paint +=1
    return paint


print(solution(8,4,[2,3,6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))
