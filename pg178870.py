# 연속된 부분 수열의 합

def solution(sequence, k):
    answer = []
    start, end = len(sequence) -1, len(sequence) -1
    sub = sequence[-1]
    while start >= 0:
        if  sub == k :
            answer = [start,end]
            start -= 1
            end -= 1
            sub += sequence[start] - sequence[end+1]
        elif sub < k :
            if  answer : break
            start -= 1
            sub += sequence[start]
        else :
            start -= 1
            end -= 1
            sub += sequence[start] - sequence[end+1]
        # print(f'start={start}, end={end}, sub={sub}, answer={answer}')
    return answer

# print(solution([1, 2, 3, 4, 5],7))
# print(solution([1, 1, 1, 2, 3, 4, 5],5))
print(solution([2, 2, 2, 2, 2],6))