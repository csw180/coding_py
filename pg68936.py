# 프로그래머스 월간코드챌린지시즌1>쿼드압축후개수세기:68936 
# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    recursive_helper = Recursive_helper()
    divide(arr, 0, 0, len(arr),recursive_helper)
    return recursive_helper.count_list 

class Recursive_helper :
    def __init__(self)  :
        self.count_list = [0,0]
    
    def add(self, lst) :
        self.count_list[0] += lst[0]
        self.count_list[1] += lst[1]

def divide(arr, x, y, n, helper):
    # print(f'{x=}, {y=}, {n=}')

    count_list =[0,0]

    for r in range(x, x+n):
        for c in range(y, y+n):
            count_list[arr[r][c]] += 1
    
    if  n == 1 or count_list[0] == 0 or count_list[1] == 0:
        helper.add([1 if arr[x][y] == 0 else 0,1 if arr[x][y] == 1 else 0])
        return
    
    divide(arr, x, y, n//2, helper)
    divide(arr, x, y+n//2, n//2, helper)
    divide(arr, x+n//2, y, n//2, helper)
    divide(arr, x+n//2, y+n//2, n//2, helper)

# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

