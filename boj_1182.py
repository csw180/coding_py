# 백준 부분수열의합:1182 https://www.acmicpc.net/problem/1182

class SubSequence :

    def __init__(self,N, target) :
        self.target = target
        self.N = N
        self.answer = 0

    def subseq(self,i, sums) :
        if  i == self.N :
            return

        sums += nums[i]
        if  sums == self.target :
            self.answer += 1

        self.subseq(i+1, sums)
        self.subseq(i+1, sums-nums[i])

    def simulation(self) :
        self.subseq(0,0)

import sys
input = sys.stdin.readline

N, S = map(int,input().split(" "))
nums = list(map(int,input().split(" ")))
subSequence = SubSequence(N,S)
subSequence.simulation()
print(subSequence.answer)
