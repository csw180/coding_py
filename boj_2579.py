import sys
cnt  = int(sys.stdin.readline().rstrip())
nums = []
for i in range(cnt) :
    nums.append(int(sys.stdin.readline().rstrip()))
nums.insert(0,0)
case1 = [0] * len(nums)    # 직전계단을 밟고 올라온 경우 점수
case2 = [0] * len(nums)    # 전전계단을 밟고 올라온 경우 점수

for i, v in enumerate(nums):
    if i==0 : continue
    if i==1 :
        case1[i] = nums[i]
        case2[i] = nums[i]
        continue

    case1[i] = case2[i-1] + nums[i]
    case2[i] = max([case1[i-2],case2[i-2]]) + nums[i]
# print(nums,case1,case2)
print(case1[len(nums)-1] if case1[len(nums)-1] > case2[len(nums)-1] else case2[len(nums)-1])