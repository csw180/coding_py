import re
def solution(st, skip, index):
    result =''
    alpa = 'abcdefghijklmnopqrstuvwxyz'*3
    dic = re.sub(rf'[{skip}]', '', alpa)    
    for s in st :
        idx = dic.find(s)
        result += dic[idx+index]
    return result