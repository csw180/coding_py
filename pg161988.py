def solution(sequence):
    seq1 = [ v * (-1 if i%2==0 else 1)  for i,v in enumerate(sequence)]
    seq2 = [ v * (1 if i%2==0 else -1)  for i,v in enumerate(sequence)]

    answer = 0
    for seq in [seq1,seq2] :
        csum = 0
        for v in seq :
            csum += v
            if csum > answer :
                answer = csum
            if csum < 0 :
                csum = 0

    return answer

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))