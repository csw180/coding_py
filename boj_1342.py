# 백준 행운의 문자열:1342  https://www.acmicpc.net/problem/1342
# python 으로 시간초과 pypy3 으로 성공

import sys

class dfs_helper() :

    def __init__(self,s) :
        self._s = s
        self._visited = [0] * len(s)
        self._answer_result = set()
    
    def add_result(self, result) :
        if  len(result) == len(self._s) :
            self._answer_result.add(result)

    def visit(self, idx) :
        self._visited[idx] = 1
        
    def unvisit(self, idx) :
        self._visited[idx] = 0
    
    def visited(self, idx) :
        return self._visited[idx]
    
    def get_answer(self) :
        return len(self._answer_result)

def dfs(idx, route, s, helper) :
   
    helper.visit(idx)
    route += s[idx]    
    for i in range(len(s)):
        exist = False
        if not helper.visited(i) and s[idx] !=  s[i] :
            exist = True
            dfs(i, route, s, helper)
    
    if  not exist :
        helper.add_result(route)

    helper.unvisit(idx)
    route = route[:-1]  
        
input  = sys.stdin.readline
s = input().rstrip()

helper = dfs_helper(s)
for i in range(len(s)):
    dfs(i,'' ,s,helper)

print(helper.get_answer())
