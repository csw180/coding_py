import re
def solution(my_string):
    return sum(map(int,re.findall(r'[0-9]',my_string)))

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))