def solution(n, left, right):
    answer = []
    d1, r1  = divmod(left,n)
    d2, r2  = divmod(right,n)
    for k  in range(d1,d2+1) :
        k_row = [(i+1 if i>k else k+1) for i in range(n)]
        # print(k_row)
        if k==d1 :
            if k==d2 :
                answer.extend(k_row[r1:r2+1])
            else :
                answer.extend(k_row[r1:])
        elif k==d2 :
            answer.extend(k_row[:r2+1])
        else :
            answer.extend(k_row)

        # print(answer)
    return answer


# print(solution(4,7,14))  # k = 1,2,3
print(solution(3,2,5))  # k = 1,2,3

