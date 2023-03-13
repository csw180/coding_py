class Cases :
    def __init__(self,used,unused) :
        self.unused = unused
        self.used = used

    def __str__(self) :
        return f'{self.used=}, {self.unused=}'

def newcase(case,choice) :
    n_case = Cases(case.used[:],case.unused[:])
    n_case.used.append(choice)
    n_case.unused.remove(choice)
    return n_case

def BFS(unused,n) :
    q = []
    result = []
    q.append(Cases([],unused))
    while q :
        cur_case = q.pop(0)
        if len(cur_case.used) < n:
            for v in cur_case.unused :   q.append(newcase(cur_case,v))
        else :
            result.append(cur_case.used)
    return result


import sys
n, m = map(int, sys.stdin.readline().split(' '))
unsed = [i for i in range(1,n+1)]
answer = BFS(unsed,m)
for i in answer :
    print(*i) 
