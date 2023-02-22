ss = "aaabbcccccca"
result=[]
stack = []
for s in ss :
    if  (not stack) or stack[-1] == s :
        stack.append(s)
    else :
        length = len(stack)
        result.append(stack.pop()+str(length))
        stack.clear()
        stack.append(s)
if stack :
    length = len(stack)
    result.append(stack.pop()+str(length))

print(''.join(result))