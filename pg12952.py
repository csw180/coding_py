#  프로그래머스 N-Qeen https://school.programmers.co.kr/learn/courses/30/lessons/12952

class dfs_helper :

    def __init__(self, n) :
        self.queens = dict()
        self.count = 0
        self.n = n

    def is_valid3(self, r,c):
        for k,v in self.queens.items() :
            if v in [c,c-r+k,c+r-k] :
                return False
        return True
    
    def dfs(self,r,step):
        if step == self.n :
            self.count += 1
            return
        for  c in range(self.n):
            if  self.is_valid3(r,c) :
                self.queens[r] = c
                self.dfs(r+1,step+1)
                del self.queens[r]
    
    def simulate(self) :
        self.dfs(0,0)

                    
def solution(n):
    helper = dfs_helper(n)
    helper.simulate()
    answer = helper.count
    return answer

print(solution(4))