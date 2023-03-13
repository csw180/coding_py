import re

def solution(dartResult:str):
    scores = [0,0,0]
    result_list = re.findall('[0-9]+[SDT]+[*#]*',dartResult)
    for i,r in enumerate(result_list) :
        score =  re.findall('[0-9]+',r)[0]
        bonus = re.findall('[SDT]+',r)[0]
        options = re.findall('[*#]+',r)
        print(f'{score=},{bonus=},{options=}')
        if len(options) > 0 :
            option = options[0]
        else :
            option = None

        scores[i] = int(score)
        if bonus== 'D' :
            scores[i] = scores[i] ** 2
        elif bonus== 'T' :
            scores[i] = scores[i] ** 3
        
        if option and option=='*' :
            scores[i] *= 2
            if i > 0 :
                scores[i-1] *= 2
        elif option and option=='#' :
            scores[i] = scores[i] * (-1)
    return sum(scores)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

