def solution(survey, choices):
    total = dict.fromkeys('RTCFJMAN', 0)
    for i, choice  in enumerate(choices) :
        score = abs(4-choice)
        agree = 0 if choice < 4 else 1  # 0: 비동의, 1: 동의
        total[survey[i][agree]] += score

    return  \
    ('R' if  total['R'] >= total['T'] else 'T'  ) + \
    ('C' if  total['C'] >= total['F'] else 'F'  ) + \
    ('J' if  total['J'] >= total['M'] else 'M'  ) + \
    ('A' if  total['A'] >= total['N'] else 'N'  ) 
    


print(solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],	[7, 1, 3]))


    # print(f'{total=}')