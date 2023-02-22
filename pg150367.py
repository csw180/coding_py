from math import ceil
    
def  btree_dfs(string) :
    if  len(string) == 1 :
        return int(string)
    
    mid = ceil(len(string) / 2)
    l = btree_dfs(string[:mid-1])
    if  l==-1 : return -1
    r = btree_dfs(string[mid:])
    if  r==-1 : return -1
    if str(l)+string[mid-1]+str(r) in ['000','111','110','011','010'] :
        return int(string[mid-1])
    else :
        return -1

def solution(numbers):
    answer = []
    for number in numbers :
        b_expr = str(bin(number))[2:]

        nsqr, size = 0 , 0
        while True :
            nsqr +=1
            size = (2 ** nsqr) -1
            if  size >= len(b_expr) :
                break
        
        b_expr = '0'* (size - len(b_expr)) + b_expr
        # print(f'{b_expr=}, len(b_expr)={len(b_expr)}')

        if  btree_dfs(b_expr) in [0,1] :
            answer.append(1)
        else :
            answer.append(0)
            
    return answer

print(solution([7, 42, 5,96]))
print(solution([63, 111, 95]))
