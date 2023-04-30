import sys

N = int(sys.stdin.readline().strip())
nums =  []
for i in range(N) :
    nums.append(sys.stdin.readline().strip())

nums.sort(key = lambda x : (len(x), x))
print(nums)
answer = 0
for i in range(len(nums)) :
    if i==len(nums)-1 and nums[i]!=nums[i-1] :
        answer += 1
        break
    starts_flag = False
    for k in range(i+1, len(nums)) :
        if nums[k].startswith(nums[i]) :
            starts_flag = True
            break
    if not starts_flag : answer += 1
print(answer)

