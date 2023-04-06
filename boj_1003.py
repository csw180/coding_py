import sys

dp =[]
dp.append((1,0))
dp.append((0,1))
for i in range(2,41) :
    dp.append((dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]))

n = int(sys.stdin.readline())
ps = []
for _ in range(n) :
    ps.append(int(sys.stdin.readline()))

for p in ps :
    print(dp[p][0],dp[p][1])
